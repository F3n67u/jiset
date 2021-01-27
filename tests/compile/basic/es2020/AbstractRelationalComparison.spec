        1. If the _LeftFirst_ flag is *true*, then
          1. Let _px_ be ? ToPrimitive(_x_, hint Number).
          1. Let _py_ be ? ToPrimitive(_y_, hint Number).
        1. Else,
          1. NOTE: The order of evaluation needs to be reversed to preserve left to right evaluation.
          1. Let _py_ be ? ToPrimitive(_y_, hint Number).
          1. Let _px_ be ? ToPrimitive(_x_, hint Number).
        1. If Type(_px_) is String and Type(_py_) is String, then
          1. If IsStringPrefix(_py_, _px_) is *true*, return *false*.
          1. If IsStringPrefix(_px_, _py_) is *true*, return *true*.
          1. Let _k_ be the smallest nonnegative integer such that the code unit at index _k_ within _px_ is different from the code unit at index _k_ within _py_. (There must be such a _k_, for neither String is a prefix of the other.)
          1. Let _m_ be the integer that is the numeric value of the code unit at index _k_ within _px_.
          1. Let _n_ be the integer that is the numeric value of the code unit at index _k_ within _py_.
          1. If _m_ < _n_, return *true*. Otherwise, return *false*.
        1. Else,
          1. If Type(_px_) is BigInt and Type(_py_) is String, then
            1. Let _ny_ be ! StringToBigInt(_py_).
            1. If _ny_ is *NaN*, return *undefined*.
            1. Return BigInt::lessThan(_px_, _ny_).
          1. If Type(_px_) is String and Type(_py_) is BigInt, then
            1. Let _nx_ be ! StringToBigInt(_px_).
            1. If _nx_ is *NaN*, return *undefined*.
            1. Return BigInt::lessThan(_nx_, _py_).
          1. NOTE: Because _px_ and _py_ are primitive values, evaluation order is not important.
          1. Let _nx_ be ? ToNumeric(_px_).
          1. Let _ny_ be ? ToNumeric(_py_).
          1. If Type(_nx_) is the same as Type(_ny_), return Type(_nx_)::lessThan(_nx_, _ny_).
          1. Assert: Type(_nx_) is BigInt and Type(_ny_) is Number, or Type(_nx_) is Number and Type(_ny_) is BigInt.
          1. If _nx_ or _ny_ is *NaN*, return *undefined*.
          1. If _nx_ is *-∞* or _ny_ is *+∞*, return *true*.
          1. If _nx_ is *+∞* or _ny_ is *-∞*, return *false*.
          1. If the mathematical value of _nx_ is less than the mathematical value of _ny_, return *true*; otherwise return *false*.