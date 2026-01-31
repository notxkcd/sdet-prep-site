---
title: "Minimum Platforms Problem"
---

The `Minimum Platforms Problem` is a classic scheduling problem that can be solved using a `greedy approach`. Given the `arrival` and `departure` times of all trains at a railway station, the goal is to find the minimum number of platforms required so that no train has to wait for a platform. It's assumed that a train occupies a platform from its arrival time until its departure time.

This problem is analogous to other resource allocation problems where resources are needed for a specific duration, and you want to minimize the total resources required.

## How it Works

### How it Works (Expanded)

The `greedy strategy` for the `Minimum Platforms Problem` involves sorting the `arrival` and `departure` times separately and then iterating through them. This allows us to track the maximum number of trains that are simultaneously present at the station.

---

Example: Arrivals = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
         Departures = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]

1. Sorted Arrivals: [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
2. Sorted Departures: [9:10, 11:20, 11:30, 12:00, 19:00, 20:00]

3. Use two pointers (i for arrival, j for departure)
- Initialize platforms = 1, max_platforms = 1
- i=1 (9:40), j=0 (9:10)

Iteration:
- Current: A[0]=9:00, D[0]=9:10. Platforms=1. Max_platforms=1.
- A[1]=9:40, D[0]=9:10.
- A[i] <= D[j]? (9:40 <= 9:10) False.
- Increment platforms (1). Max_platforms = max(1,1)=1. Increment j (D[0] used).
- A[1]=9:40, D[1]=11:20.
- A[i] <= D[j]? (9:40 <= 11:20) True.
- Increment platforms (2). Max_platforms = max(2,1)=2. Increment i.
- A[2]=9:50, D[1]=11:20.
- A[i] <= D[j]? (9:50 <= 11:20) True.
- Increment platforms (3). Max_platforms = max(3,2)=3. Increment i.
- A[3]=11:00, D[1]=11:20.
- A[i] <= D[j]? (11:00 <= 11:20) True.
- Increment platforms (4). Max_platforms = max(4,3)=4. Increment i.
- A[4]=15:00, D[1]=11:20.
- A[i] <= D[j]? (15:00 <= 11:20) False.
- Decrement platforms (3). Max_platforms = max(3,4)=4. Increment j.
- ... and so on.

The logic effectively counts how many trains are at the station at any given point in time.
The maximum concurrent count is the minimum platforms needed.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def min_platforms(arrival_times, departure_times):
    """
    Solves the Minimum Platforms Problem.
    <code>arrival_times</code>: a list of arrival times.
    <code>departure_times</code>: a list of departure times.
    Assumes arrival_times and departure_times are lists of numbers
    (e.g., minutes from midnight).
    """
    n = len(arrival_times)
    
    # 1. Sort arrival and departure times
    arrival_times.sort()
    departure_times.sort()

    platforms_needed = 0
    max_platforms = 0
    
    i = 0 # Pointer for arrival times
    j = 0 # Pointer for departure times

    # 2. Iterate through sorted times
    while i < n and j < n:
        if arrival_times[i] <= departure_times[j]:
            # A train arrives, so a platform is needed
            platforms_needed += 1
            i += 1
        else:
            # A train departs, freeing up a platform
            platforms_needed -= 1
            j += 1
        
        # Update maximum platforms needed so far
        max_platforms = max(max_platforms, platforms_needed)
            
    return max_platforms

# Example
# arrival = [900, 940, 950, 1100, 1500, 1800] # Times in HHMM format (e.g., 9:00 is 900)
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# print(min_platforms(arrival, departure)) # Expected: 3
```

### Javascript

```javascript
function minPlatforms(arrivalTimes, departureTimes) {
    /*<em>
     </em> Solves the Minimum Platforms Problem.
     <em> <code>arrivalTimes</code>: an array of arrival times.
     </em> <code>departureTimes</code>: an array of departure times.
     <em> Assumes times are numbers (e.g., minutes from midnight).
     </em>/
    const n = arrivalTimes.length;
    
    // 1. Sort arrival and departure times
    arrivalTimes.sort((a, b) => a - b);
    departureTimes.sort((a, b) => a - b);

    let platformsNeeded = 0;
    let maxPlatforms = 0;
    
    let i = 0; // Pointer for arrival times
    let j = 0; // Pointer for departure times

    // 2. Iterate through sorted times
    while (i < n && j < n) {
        if (arrivalTimes[i] <= departureTimes[j]) {
            // A train arrives, so a platform is needed
            platformsNeeded++;
            i++;
        } else {
            // A train departs, freeing up a platform
            platformsNeeded--;
            j++;
        }
        
        // Update maximum platforms needed so far
        maxPlatforms = Math.max(maxPlatforms, platformsNeeded);
    }
            
    return maxPlatforms;
}

// const arrival = [900, 940, 950, 1100, 1500, 1800];
// const departure = [910, 1200, 1120, 1130, 1900, 2000];
// console.log(minPlatforms(arrival, departure)); // Expected: 3
```

### Typescript

```typescript
function minPlatformsTS(arrivalTimes: number[], departureTimes: number[]): number {
    /*<em>
     </em> Solves the Minimum Platforms Problem.
     <em> <code>arrivalTimes</code>: an array of arrival times.
     </em> <code>departureTimes</code>: an array of departure times.
     <em> Assumes times are numbers (e.g., minutes from midnight).
     </em>/
    const n = arrivalTimes.length;
    
    // 1. Sort arrival and departure times
    arrivalTimes.sort((a, b) => a - b);
    departureTimes.sort((a, b) => a - b);

    let platformsNeeded = 0;
    let maxPlatforms = 0;
    
    let i = 0; // Pointer for arrival times
    let j = 0; // Pointer for departure times

    // 2. Iterate through sorted times
    while (i < n && j < n) {
        if (arrivalTimes[i] <= departureTimes[j]) {
            // A train arrives, so a platform is needed
            platformsNeeded++;
            i++;
        } else {
            // A train departs, freeing up a platform
            platformsNeeded--;
            j++;
        }
        
        // Update maximum platforms needed so far
        maxPlatforms = Math.max(maxPlatforms, platformsNeeded);
    }
            
    return maxPlatforms;
}

// const arrivalTS = [900, 940, 950, 1100, 1500, 1800];
// const departureTS = [910, 1200, 1120, 1130, 1900, 2000];
// console.log(minPlatformsTS(arrivalTS, departureTS)); // Expected: 3
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::sort, std::max

int minPlatforms(std::vector<int> arrival_times, std::vector<int> departure_times) {
    int n = arrival_times.size();
    
    // 1. Sort arrival and departure times
    std::sort(arrival_times.begin(), arrival_times.end());
    std::sort(departure_times.begin(), departure_times.end());

    int platforms_needed = 0;
    int max_platforms = 0;
    
    int i = 0; // Pointer for arrival times
    int j = 0; // Pointer for departure times

    // 2. Iterate through sorted times
    while (i < n && j < n) {
        if (arrival_times[i] <= departure_times[j]) {
            // A train arrives, so a platform is needed
            platforms_needed++;
            i++;
        } else {
            // A train departs, freeing up a platform
            platforms_needed--;
            j++;
        }
        
        // Update maximum platforms needed so far
        max_platforms = std::max(max_platforms, platforms_needed);
    }
            
    return max_platforms;
}

// int main() {
//     std::vector<int> arrival = {900, 940, 950, 1100, 1500, 1800};
//     std::vector<int> departure = {910, 1200, 1120, 1130, 1900, 2000};
//     std::cout << "Minimum platforms needed: " << minPlatforms(arrival, departure) << std::endl; // 3
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "sort"
)

func minPlatforms(arrivalTimes, departureTimes []int) int {
    n := len(arrivalTimes)
    
    // 1. Sort arrival and departure times
    sort.Ints(arrivalTimes)
    sort.Ints(departureTimes)

    platformsNeeded := 0
    maxPlatforms := 0
    
    i := 0 // Pointer for arrival times
    j := 0 // Pointer for departure times

    // 2. Iterate through sorted times
    for i < n && j < n {
        if arrivalTimes[i] <= departureTimes[j] {
            // A train arrives, so a platform is needed
            platformsNeeded++
            i++
        } else {
            // A train departs, freeing up a platform
            platformsNeeded--
            j++
        }
        
        // Update maximum platforms needed so far
        maxPlatforms = max(maxPlatforms, platformsNeeded)
    }
            
    return maxPlatforms
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     arrival := []int{900, 940, 950, 1100, 1500, 1800}
//     departure := []int{910, 1200, 1120, 1130, 1900, 2000}
//     fmt.Println("Minimum platforms needed:", minPlatforms(arrival, departure)) // 3
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort, max

int minPlatforms(int[] arrivalTimes, int[] departureTimes) {
    auto n = arrivalTimes.length;
    
    // 1. Sort arrival and departure times
    arrivalTimes.sort();
    departureTimes.sort();

    int platformsNeeded = 0;
    int maxPlatforms = 0;
    
    int i = 0; // Pointer for arrival times
    int j = 0; // Pointer for departure times

    // 2. Iterate through sorted times
    while (i < n && j < n) {
        if (arrivalTimes[i] <= departureTimes[j]) {
            // A train arrives, so a platform is needed
            platformsNeeded++;
            i++;
        } else {
            // A train departs, freeing up a platform
            platformsNeeded--;
            j++;
        }
        
        // Update maximum platforms needed so far
        maxPlatforms = max(maxPlatforms, platformsNeeded);
    }
            
    return maxPlatforms;
}

// void main() {
//     auto arrival = [900, 940, 950, 1100, 1500, 1800];
//     auto departure = [910, 1200, 1120, 1130, 1900, 2000];
//     writeln("Minimum platforms needed: ", minPlatforms(arrival, departure)); // 3
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Minimum Platforms Problem` is solved by a `greedy approach` that efficiently tracks the maximum number of concurrent events using sorted `arrival` and `departure` times.

---

**`min_platforms(arrival_times, departure_times)` Function:**
- `arrival_times`: A list of train arrival times.
- `departure_times`: A list of train departure times (corresponding to `arrival_times`).

**Algorithm Steps:**
- **Sort Times:** Both the `arrival_times` and `departure_times` arrays are sorted in non-decreasing order. This is a crucial preprocessing step for the greedy strategy.
- **Initialize Pointers and Counters:**
- `platforms_needed`: Keeps track of the currently occupied platforms.
- `max_platforms`: Stores the maximum value `platforms_needed` has reached, which will be the result.
- `i`: A pointer for the `arrival_times` array, starting at index 0.
- `j`: A pointer for the `departure_times` array, starting at index 0.

    </li>
- **Scan Times Greedily:** A `while` loop iterates as long as both pointers are within the bounds of their respective arrays.
- **If `arrival_times[i] <= departure_times[j]`:**
- This means a train is arriving (or two trains arrive and depart at the same time). A new platform will be needed.
- `platforms_needed` is incremented.
- `i` is incremented to consider the next arrival.

            </li>
- **Else (`arrival_times[i] > departure_times[j]`):**
- This means a train has departed before a new one arrives. A platform becomes free.
- `platforms_needed` is decremented.
- `j` is incremented to consider the next departure.

            </li>
- After each step (arrival or departure), `max_platforms` is updated to be the maximum of its current value and `platforms_needed`. This captures the peak concurrent platform usage.

    </li>

**Result:**
- The final `max_platforms` value is the minimum number of platforms required.

[Back to Implementation](#implementation)

## Applications

### Application

The `Minimum Platforms Problem` is a classic example of how a greedy approach can solve scheduling and resource allocation problems efficiently. It has direct analogies in various fields:
- **Meeting Room Scheduling:** Determining the minimum number of meeting rooms required to accommodate a given set of meetings with their start and end times.
- **Operating System Task Scheduling:** Calculating the minimum number of CPUs or processing units needed to handle a set of tasks, each with an arrival and completion time.
- **Event Management:** Planning an event with multiple sessions/performances and determining the minimum number of stages or venues required to avoid overlaps.
- **Cloud Computing Resource Allocation:** Optimizing the number of virtual machines or server instances needed to handle fluctuating workloads.
- **Traffic Management:** Optimizing the number of lanes or gates required at airports or toll booths during peak hours.

