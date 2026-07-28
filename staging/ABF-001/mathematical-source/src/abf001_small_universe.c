#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define FUNCTIONS (1u << 16)
#define EXPECTED_COMPARISONS (65536ull * 14ull * 3ull * 2ull)

static inline unsigned parity_u32(uint32_t x) {
    return (unsigned)(__builtin_popcount(x) & 1u);
}

static void kernel_basis(unsigned a, unsigned *u_out, unsigned *v_out) {
    unsigned u = 0, v = 0;
    for (unsigned x = 1; x < 8; ++x) {
        if (parity_u32(a & x) == 0u) {
            if (u == 0u) u = x;
            else if (x != u) { v = x; break; }
        }
    }
    if (u == 0u || v == 0u || u == v) {
        fprintf(stderr, "kernel basis failure for a=%u\n", a);
        exit(2);
    }
    *u_out = u;
    *v_out = v;
}

static void affine_points(unsigned a, unsigned b, unsigned points[4]) {
    unsigned p0 = 8;
    for (unsigned x = 0; x < 8; ++x) {
        if (parity_u32(a & x) == b) { p0 = x; break; }
    }
    if (p0 == 8) { fprintf(stderr, "no affine point\n"); exit(2); }
    unsigned u, v;
    kernel_basis(a, &u, &v);
    points[0] = p0;
    points[1] = p0 ^ u;
    points[2] = p0 ^ v;
    points[3] = p0 ^ u ^ v;
    for (unsigned i = 0; i < 4; ++i) {
        for (unsigned j = i + 1; j < 4; ++j) {
            if (points[i] == points[j]) {
                fprintf(stderr, "duplicate point\n"); exit(2);
            }
        }
    }
}

static inline unsigned scalar_value(uint16_t function, unsigned x, unsigned mask) {
    unsigned output = (function >> (2u * x)) & 3u;
    return parity_u32(output & mask);
}

static int anf_degree_four(const unsigned values_in[4]) {
    unsigned c0 = values_in[0];
    unsigned c1 = values_in[1] ^ values_in[0];
    unsigned c2 = values_in[2] ^ values_in[0];
    unsigned c3 = values_in[3] ^ values_in[2] ^ values_in[1] ^ values_in[0];
    int degree = -1;
    if (c0) degree = 0;
    if (c1 || c2) degree = 1;
    if (c3) degree = 2;
    return degree;
}

static int moments_vanish(uint16_t function, const unsigned points[4], unsigned mask, unsigned order) {
    unsigned total = 0;
    for (unsigned i = 0; i < 4; ++i) total ^= scalar_value(function, points[i], mask);
    if (total) return 0;
    if (order == 0u) return 1;
    for (unsigned coordinate = 0; coordinate < 3; ++coordinate) {
        total = 0;
        for (unsigned i = 0; i < 4; ++i) {
            if ((points[i] >> coordinate) & 1u) total ^= scalar_value(function, points[i], mask);
        }
        if (total) return 0;
    }
    return 1;
}

int main(void) {
    unsigned hpoints[14][4];
    unsigned h = 0;
    for (unsigned a = 1; a < 8; ++a) {
        for (unsigned b = 0; b < 2; ++b) {
            affine_points(a, b, hpoints[h]);
            ++h;
        }
    }
    uint64_t comparisons = 0;
    uint64_t failures = 0;
    clock_t start = clock();
    for (uint32_t function = 0; function < FUNCTIONS; ++function) {
        for (unsigned hi = 0; hi < 14; ++hi) {
            const unsigned *points = hpoints[hi];
            for (unsigned mask = 1; mask <= 3; ++mask) {
                unsigned values[4];
                for (unsigned i = 0; i < 4; ++i) values[i] = scalar_value((uint16_t)function, points[i], mask);
                int degree = anf_degree_four(values);
                for (unsigned order = 0; order <= 1; ++order) {
                    int threshold = 1 - (int)order;
                    int direct = degree <= threshold;
                    int moment = moments_vanish((uint16_t)function, points, mask, order);
                    ++comparisons;
                    if (direct != moment) {
                        ++failures;
                        if (failures <= 20) {
                            fprintf(stderr, "mismatch function=%04x hyperplane=%u mask=%u order=%u degree=%d direct=%d moment=%d\n",
                                    function, hi, mask, order, degree, direct, moment);
                        }
                    }
                }
            }
        }
    }
    double elapsed = (double)(clock() - start) / (double)CLOCKS_PER_SEC;
    if (comparisons != EXPECTED_COMPARISONS || failures != 0) {
        fprintf(stderr, "FAIL comparisons=%llu expected=%llu failures=%llu\n",
                (unsigned long long)comparisons,
                (unsigned long long)EXPECTED_COMPARISONS,
                (unsigned long long)failures);
        return 1;
    }
    printf("{\n");
    printf("  \"schema_version\": \"n.human_llm.mathematics.abf001.small_universe_c.v1\",\n");
    printf("  \"result\": \"PASS\",\n");
    printf("  \"maps\": 65536,\n");
    printf("  \"affine_hyperplanes_per_map\": 14,\n");
    printf("  \"nonzero_output_masks\": 3,\n");
    printf("  \"moment_orders\": [0, 1],\n");
    printf("  \"comparisons\": %llu,\n", (unsigned long long)comparisons);
    printf("  \"failures\": 0,\n");
    printf("  \"elapsed_cpu_seconds\": %.6f\n", elapsed);
    printf("}\n");
    return 0;
}
