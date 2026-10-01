#include <cinttypes>
#include <cstdio>

#include "challenge_api.h"

int main()
{
    const std::uint32_t result = challenge_compute(configured_student_id());
    std::puts(configured_student_label());
    if (result == 0) {
        std::puts("Invalid student ID.");
    } else {
        std::printf("Result: %" PRIu32 "\n", result);
    }
    std::puts("Press Enter to exit...");
    std::fflush(stdout);
    std::getchar();
    return result == 0 ? 1 : 0;
}
