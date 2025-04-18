#include <vector>
#include <string>
#include <tuple>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

inline ll true_mod(ll x, ll mod) {
    ll res = x % mod;
    return res < 0 ? res + mod : res;
}

template<ll P, ll Mod>
struct phash {
    static ll const mod = Mod;
    static ll const p = P;

    phash(ll value) : value(value) {}
    phash(size_t maxn, bool) { pw(maxn, true); } // Нетривиальный хак статических полей

    static ll pw(int d, bool check = false) {
        static vector<ll> power{1};
        while (check && power.size() <= d)
            power.push_back(power.back() * p % mod);
        return power[d];
    }

    phash<P, Mod> operator+(char c) const { return {(value * p + c - 'a' + 1) % mod}; }
    phash<P, Mod> operator+=(char c) { return *this = *this + c; }

    template<ll P2, ll Mod2>
    bool operator==(phash<P2, Mod2> const &other) const = delete;
    template<ll P2, ll Mod2>
    bool operator!=(phash<P2, Mod2> const &other) const = delete;

    bool operator==(phash<P, Mod> const &other) const { return value == other.value; }
    bool operator!=(phash<P, Mod> const &other) const { return value != other.value; }
    operator ll() const { return value; }

private:
    ll value = 0;
};

namespace helper {
    template<typename Tuple, size_t ...Is>
    Tuple __append_impl(char c, Tuple const &t, index_sequence<Is...>) {
        return Tuple((get<Is>(t) + c)...);
    }

    template<typename Tuple>
    Tuple append(char c, Tuple const &t) {
        return __append_impl(c, t, make_index_sequence<tuple_size_v<Tuple>>{});
    }

    template<typename Tuple, size_t ...Is>
    Tuple __subtract_impl(int len, Tuple const &l, Tuple const &r, index_sequence<Is...>) {
        return Tuple(true_mod(
                get<Is>(r) - get<Is>(l) * decay_t<decltype(get<Is>(l))>::pw(len),
                decay_t<decltype(get<Is>(l))>::mod
        )...);
    }

    template<typename Tuple>
    Tuple subtract(int len, Tuple const &l, Tuple const &r) {
        return __subtract_impl(len, l, r, make_index_sequence<tuple_size_v<Tuple>>{});
    }
}

template<typename ...Ts>
struct hstring {
    string _s;
    vector<tuple<Ts...>> h;

    template<typename P>
    hstring(P &&p) : _s(p) { __init(); }

    tuple<Ts...> subhash(int l, int r) const { // В 0-индексации, запрос - полуинтервал
        auto left = h[l], right = h[r];
        return helper::subtract(r - l, left, right);
    }

private:
    void __init() {
        tuple<Ts...> t(Ts(_s.length(), false)...);
        h.push_back(t);
        int iter = 0;
        generate_n(back_inserter(h), _s.size(), [&]() {
            return helper::append(_s[iter++], h.back());
        });
    }
};

int main() {

    typedef phash<31, 1000000007> h1;
    typedef phash<37, 1000000009> h2;
    typedef hstring<h1, h2> hs;

    hs s1 = "abacaba", s2 = "abracadabra";
    auto test = [](hs const &s1, int l1, int r1, hs const &s2, int l2, int r2) {
        cout << s1._s.substr(l1, r1 - l1) << " vs " << s2._s.substr(l2, r2 - l2) << ": ";
        auto sh1 = s1.subhash(l1, r1), sh2 = s2.subhash(l2, r2);
        cout << (sh1 == sh2 ? "true" : "false") << '\n';
    };

    test(s1, 0, 3, s1, 4, 7);
    test(s2, 0, 4, s2, 7, 11);
    test(s1, 2, 5, s2, 3, 6);
    test(s1, 4, 7, s2, 7, 10);
    test(s1, 3, 7, s2, 4, 8);

    hstring<h1> s3 = "a";
    hstring<h2> s4 = "a";
    // cout << (s3.subhash(0, 1) == s4.subhash(0, 1)) << '\n';
    // не компилируется, не тот тип (чтобы нельзя было случайно набагать, сравнивая разные хэши)

}
