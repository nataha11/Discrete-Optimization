#include <iostream>
#include <algorithm>

using namespace std;

struct Item {
    int weight;
    int value;
    double dens;
};

int opt_value = 0;

bool cmpItem(Item rhs, Item lhs) {
    return rhs.dens > lhs.dens;
}

void solve_with_lp(int k, int total_knapsack_volume, int possible_weight, const Item * items, int val) {
    
    int possible_value = 0;
    int w_left = possible_weight;
    for (int i = k; i < total_knapsack_volume; i++) {
        if (w_left >= items[i].weight) {
            w_left -= items[i].weight;
            possible_value += items[i].value;
        } else {
            possible_value += int(items[i].dens * w_left);
        }
    }
    
    if (k < total_knapsack_volume && possible_value + val > opt_value) {
        possible_value -= items[k].value;
        solve_with_lp(k + 1, total_knapsack_volume, possible_weight, items, val);
        if (items[k].weight <= possible_weight) {
            possible_weight -= items[k].weight;
            val += items[k].value;
            if (val > opt_value) {
                opt_value = val;
            }
            solve_with_lp(k + 1, total_knapsack_volume, possible_weight, items, val);
        }
    }
    return;
}

int main(void) {
    
    /* Input data */
    int total_knapsack_volume = 0, number_of_items = 0;
    cin >> total_knapsack_volume;
    cin >> number_of_items;
    
    Item items[number_of_items];
    
    for (int i = 0; i < number_of_items; i++) {
        cin >> items[i].weight;
        cin >> items[i].value;
        items[i].dens = 1.0 * items[i].value / items[i].weight;
    }
    
    /* Sort items by dens */
    sort(items, items + number_of_items, cmpItem);

    /* lower_value is obtained by the greedy algorithm */
    int weight_left = total_knapsack_volume;
    int lower_value = 0;
    
    for (int i = 0; i < number_of_items; i++) {
        if (weight_left >= items[i].weight) {
            weight_left -= items[i].weight;
            lower_value += items[i].value;
        }
    }
    
    opt_value = lower_value;
    
    /* Find optimal value */
    solve_with_lp(0, number_of_items, total_knapsack_volume, items, 0);
    
    cout << opt_value << endl;
    
    return 0;
}    