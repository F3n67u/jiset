          1. Let _x_ be ? thisNumberValue(*this* value).
          1. If _precision_ is *undefined*, return ! ToString(_x_).
          1. Let _p_ be ? ToInteger(_precision_).
          1. If _x_ is *NaN*, return the String `"NaN"`.
          1. Let _s_ be the empty String.
          1. If _x_ < 0, then
            1. Let _s_ be the code unit 0x002D (HYPHEN-MINUS).
            1. Let _x_ be -_x_.
          1. If _x_ = *+∞*, then
            1. Return the string-concatenation of _s_ and `"Infinity"`.
          1. If _p_ < 1 or _p_ > 100, throw a *RangeError* exception.
          1. If _x_ = 0, then
            1. Let _m_ be the String value consisting of _p_ occurrences of the code unit 0x0030 (DIGIT ZERO).
            1. Let _e_ be 0.
          1. Else _x_ ≠ 0,
            1. Let _e_ and _n_ be integers such that 10<sup>_p_-1</sup> ≤ _n_ < 10<sup>_p_</sup> and for which the exact mathematical value of _n_ × 10<sup>_e_-_p_+1</sup> - _x_ is as close to zero as possible. If there are two such sets of _e_ and _n_, pick the _e_ and _n_ for which _n_ × 10<sup>_e_-_p_+1</sup> is larger.
            1. Let _m_ be the String value consisting of the digits of the decimal representation of _n_ (in order, with no leading zeroes).
            1. If _e_ < -6 or _e_ ≥ _p_, then
              1. Assert: _e_ ≠ 0.
              1. If _p_ ≠ 1, then
                1. Let _a_ be the first element of _m_, and let _b_ be the remaining _p_-1 elements of _m_.
                1. Let _m_ be the string-concatenation of _a_, `"."`, and _b_.
              1. If _e_ > 0, then
                1. Let _c_ be the code unit 0x002B (PLUS SIGN).
              1. Else _e_ < 0,
                1. Let _c_ be the code unit 0x002D (HYPHEN-MINUS).
                1. Let _e_ be -_e_.
              1. Let _d_ be the String value consisting of the digits of the decimal representation of _e_ (in order, with no leading zeroes).
              1. Return the string-concatenation of _s_, _m_, the code unit 0x0065 (LATIN SMALL LETTER E), _c_, and _d_.
          1. If _e_ = _p_-1, return the string-concatenation of _s_ and _m_.
          1. If _e_ ≥ 0, then
            1. Let _m_ be the string-concatenation of the first _e_+1 elements of _m_, the code unit 0x002E (FULL STOP), and the remaining _p_- (_e_+1) elements of _m_.
          1. Else _e_ < 0,
            1. Let _m_ be the string-concatenation of the code unit 0x0030 (DIGIT ZERO), the code unit 0x002E (FULL STOP), -(_e_+1) occurrences of the code unit 0x0030 (DIGIT ZERO), and the String _m_.
          1. Return the string-concatenation of _s_ and _m_.