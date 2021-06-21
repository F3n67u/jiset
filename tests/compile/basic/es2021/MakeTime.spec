          1. If _hour_ is not finite or _min_ is not finite or _sec_ is not finite or _ms_ is not finite, return *NaN*.
          1. Let _h_ be 𝔽(! ToIntegerOrInfinity(_hour_)).
          1. Let _m_ be 𝔽(! ToIntegerOrInfinity(_min_)).
          1. Let _s_ be 𝔽(! ToIntegerOrInfinity(_sec_)).
          1. Let _milli_ be 𝔽(! ToIntegerOrInfinity(_ms_)).
          1. Let _t_ be ((_h_ `*` msPerHour `+` _m_ `*` msPerMinute) `+` _s_ `*` msPerSecond) `+` _milli_, performing the arithmetic according to IEEE 754-2019 rules (that is, as if using the ECMAScript operators `*` and `+`).
          1. Return _t_.