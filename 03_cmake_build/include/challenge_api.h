#pragma once

#include <cstdint>

// Returns zero for invalid input; valid results are six-digit numbers.
extern "C" std::uint32_t challenge_compute(const char* student_id);

const char* configured_student_id();
const char* configured_student_label();
