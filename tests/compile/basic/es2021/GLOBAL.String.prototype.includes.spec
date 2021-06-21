          1. Let _O_ be ? RequireObjectCoercible(*this* value).
          1. Let _S_ be ? ToString(_O_).
          1. Let _isRegExp_ be ? IsRegExp(_searchString_).
          1. If _isRegExp_ is *true*, throw a *TypeError* exception.
          1. Let _searchStr_ be ? ToString(_searchString_).
          1. Let _pos_ be ? ToIntegerOrInfinity(_position_).
          1. Assert: If _position_ is *undefined*, then _pos_ is 0.
          1. Let _len_ be the length of _S_.
          1. Let _start_ be the result of clamping _pos_ between 0 and _len_.
          1. Let _index_ be ! StringIndexOf(_S_, _searchStr_, _start_).
          1. If _index_ is not -1, return *true*.
          1. Return *false*.