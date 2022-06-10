#include "include.h"

template <typename T>
pair<float, float> one_step (const pair<float, float> coefs, const pair<T, T> coords, const float alpha) {
    float p, y, error;
    p = coefs.first + coefs.second*coords.first;
    y = coords.second;
    error = p - y;
    // cout << "Predict: " << p << endl << "Y: " << y << endl;
    pair<float, float> new_coefs;
    new_coefs.first = coefs.first - alpha*error;
    new_coefs.second = coefs.second - alpha*coords.first*error;
    return new_coefs;
}

template <typename T>
pair<float, float> lr(const vector<pair<T, T>> coords) {
    const int eras_count = 8;
    const int population = coords.size();
    const float alpha = 0.01;
    pair<float, float> coefs = make_pair (0, 1);
    for (int era = 0; era < eras_count; era++) {
        for (const pair<T, T> point: coords) {
            coefs = one_step<T>(coefs, point, alpha);
        }
    }
    return coefs;
}

int main() {
    int n, x, y;
    pair<int, int> xy;
    pair<float, float> result_coefs;
    vector<pair<int, int>> coords;
    cout << "Enter count of points" << endl;
    cin >> n;
    coords.reserve(n);
    cout << "Enter coordinates" << endl;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        xy.first = x;
        xy.second = y;
        coords.push_back(xy);
    }
    result_coefs = lr<int>(coords);
    cout << result_coefs.first << ' ' << result_coefs.second;
    return 0;
}