#include <iostream>

class Counter {
private:
    int count;

public:
    // Constructor
    Counter(int initial_count = 0) : count(initial_count) {}

    // Overload the () operator to increment the count
    void operator()() {
        ++count;
    }

    // Method to decrement the count
    void decrement() {
        --count;
    }

    // Method to reset the count
    void reset() {
        count = 0;
    }

    // Method to get the current count
    int getCount() const {
        return count;
    }
};

int main() {
    Counter counter;

    // Using the overloaded () operator to increment the count
    counter();
    counter();
    std::cout << "Count after incrementing twice: " << counter.getCount() << std::endl;  // Output: 2

    // Decrement the count
    counter.decrement();
    std::cout << "Count after decrementing: " << counter.getCount() << std::endl;  // Output: 1

    // Reset the count
    counter.reset();
    std::cout << "Count after resetting: " << counter.getCount() << std::endl;  // Output: 0

    return 0;
}
