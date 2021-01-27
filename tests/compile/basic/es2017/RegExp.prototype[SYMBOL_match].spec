          1. Let _rx_ be the *this* value.
          1. If Type(_rx_) is not Object, throw a *TypeError* exception.
          1. Let _S_ be ? ToString(_string_).
          1. Let _global_ be ToBoolean(? Get(_rx_, `"global"`)).
          1. If _global_ is *false*, then
            1. Return ? RegExpExec(_rx_, _S_).
          1. Else _global_ is *true*,
            1. Let _fullUnicode_ be ToBoolean(? Get(_rx_, `"unicode"`)).
            1. Perform ? Set(_rx_, `"lastIndex"`, 0, *true*).
            1. Let _A_ be ! ArrayCreate(0).
            1. Let _n_ be 0.
            1. Repeat,
              1. Let _result_ be ? RegExpExec(_rx_, _S_).
              1. If _result_ is *null*, then
                1. If _n_=0, return *null*.
                1. Return _A_.
              1. Else _result_ is not *null*,
                1. Let _matchStr_ be ? ToString(? Get(_result_, `"0"`)).
                1. Let _status_ be CreateDataProperty(_A_, ! ToString(_n_), _matchStr_).
                1. Assert: _status_ is *true*.
                1. If _matchStr_ is the empty String, then
                  1. Let _thisIndex_ be ? ToLength(? Get(_rx_, `"lastIndex"`)).
                  1. Let _nextIndex_ be AdvanceStringIndex(_S_, _thisIndex_, _fullUnicode_).
                  1. Perform ? Set(_rx_, `"lastIndex"`, _nextIndex_, *true*).
                1. Increment _n_.