---
title: "Activity Selection Problem"
---

The `Activity Selection Problem` is a classic optimization problem that demonstrates the effectiveness of a `greedy approach`. Given a set of `activities`, each with a `start time` and a `finish time`, the goal is to select the maximum number of non-overlapping `activities` that can be performed by a single resource (e.g., a person, a machine, or a classroom). All activities are assumed to be sorted by their finish times.

The problem can be solved efficiently by repeatedly choosing the `activity` that finishes earliest among the remaining compatible activities, thus leaving the maximum time available for subsequent activities.

## How it Works

### How it Works (Expanded)

The `greedy choice` in the `Activity Selection Problem` is to always pick the `activity` that finishes earliest among the available options. This is a crucial step that needs to be proven correct for the `greedy approach` to work.

**Proof Sketch of Greedy Choice:**
    Suppose we have an optimal solution `OPT`. Let `a_1` be the activity in `OPT` with the earliest finish time. Let `a_k` be the activity with the earliest finish time in the entire set of activities `S`. If `a_1 = a_k`, then our greedy choice aligns with `OPT`. If `a_1 != a_k`, we can swap `a_1` with `a_k` to form a new solution `OPT'` that is still optimal (it has the same number of activities) and `a_k` is now included. This means there's always an optimal solution that contains the greedy choice.

---

Example: Activities = [ (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16) ]

1. Sort by finish times: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)
   Activities (Start, Finish):
   A1: (1,4)
   A2: (3,5)
   A3: (0,6)
   A4: (5,7)
   A5: (3,9)
   A6: (5,9)
   A7: (6,10)
   A8: (8,11)
   A9: (8,12)
   A10: (2,14)
   A11: (12,16)

2. Select activities:
- Pick A1 (1,4). Last finish time = 4.
- Next activity with start time >= 4 is A4 (5,7). Pick A4. Last finish time = 7.
- Next activity with start time >= 7 is A8 (8,11). Pick A8. Last finish time = 11.
- Next activity with start time >= 11 is A11 (12,16). Pick A11. Last finish time = 16.

Selected Activities: (1,4), (5,7), (8,11), (12,16). Total 4 activities.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def activity_selection(activities):
    """
    Solves the Activity Selection Problem.
    <code>activities</code>: a list of tuples, where each tuple is (start_time, finish_time).
                  Assumes activities are already sorted by finish_time.
    """
    if not activities:
        return []

    # Sort activities by finish time (if not already sorted)
    # activities.sort(key=lambda x: x[1])

    selected_activities = []
    
    # Select the first activity
    selected_activities.append(activities[0])
    last_finish_time = activities[0][1]

    # Iterate through the remaining activities
    for i in range(1, len(activities)):
        current_activity_start_time = activities[i][0]
        current_activity_finish_time = activities[i][1]

        # If this activity can be selected (doesn't overlap with the last selected one)
        if current_activity_start_time >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = current_activity_finish_time
            
    return selected_activities

# Example: Activities sorted by finish time
# activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# print(activity_selection(activities)) # Expected: [(1, 4), (5, 7), (8, 11), (12, 16)]
```

### Javascript

```javascript
function activitySelection(activities) {
    /*<em>
     </em> Solves the Activity Selection Problem.
     <em> <code>activities</code>: an array of objects, where each object is { start: number, finish: number }.
     </em>               Assumes activities are already sorted by finish_time.
     <em>/
    if (activities.length === 0) {
        return [];
    }

    // Sort activities by finish time (if not already sorted)
    // activities.sort((a, b) => a.finish - b.finish);

    const selectedActivities = [];
    
    // Select the first activity
    selectedActivities.push(activities[0]);
    let lastFinishTime = activities[0].finish;

    // Iterate through the remaining activities
    for (let i = 1; i < activities.length; i++) {
        const currentActivity = activities[i];

        // If this activity can be selected (doesn't overlap with the last selected one)
        if (currentActivity.start >= lastFinishTime) {
            selectedActivities.push(currentActivity);
            lastFinishTime = currentActivity.finish;
        }
    }
            
    return selectedActivities;
}

// const activities = [
//     { start: 1, finish: 4 }, { start: 3, finish: 5 }, { start: 0, finish: 6 },
//     { start: 5, finish: 7 }, { start: 3, finish: 9 }, { start: 5, finish: 9 },
//     { start: 6, finish: 10 }, { start: 8, finish: 11 }, { start: 8, finish: 12 },
//     { start: 2, finish: 14 }, { start: 12, finish: 16 }
// ];
// console.log(activitySelection(activities)); 
// Expected: [{start: 1, finish: 4}, {start: 5, finish: 7}, {start: 8, finish: 11}, {start: 12, finish: 16}]
```

### Typescript

```typescript
interface Activity {
    start: number;
    finish: number;
}

function activitySelectionTS(activities: Activity[]): Activity[] {
    /</em><em>
     </em> Solves the Activity Selection Problem.
     <em> <code>activities</code>: an array of objects, where each object is { start: number, finish: number }.
     </em>               Assumes activities are already sorted by finish_time.
     */
    if (activities.length === 0) {
        return [];
    }

    // Sort activities by finish time (if not already sorted)
    // activities.sort((a, b) => a.finish - b.finish);

    const selectedActivities: Activity[] = [];
    
    // Select the first activity
    selectedActivities.push(activities[0]);
    let lastFinishTime = activities[0].finish;

    // Iterate through the remaining activities
    for (let i = 1; i < activities.length; i++) {
        const currentActivity = activities[i];

        // If this activity can be selected (doesn't overlap with the last selected one)
        if (currentActivity.start >= lastFinishTime) {
            selectedActivities.push(currentActivity);
            lastFinishTime = currentActivity.finish;
        }
    }
            
    return selectedActivities;
}

// const activitiesTS: Activity[] = [
//     { start: 1, finish: 4 }, { start: 3, finish: 5 }, { start: 0, finish: 6 },
//     { start: 5, finish: 7 }, { start: 3, finish: 9 }, { start: 5, finish: 9 },
//     { start: 6, finish: 10 }, { start: 8, finish: 11 }, { start: 8, finish: 12 },
//     { start: 2, finish: 14 }, { start: 12, finish: 16 }
// ];
// console.log(activitySelectionTS(activitiesTS)); 
// Expected: [{start: 1, finish: 4}, {start: 5, finish: 7}, {start: 8, finish: 11}, {start: 12, finish: 16}]
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::sort

// Struct to represent an activity
struct Activity {
    int start;
    int finish;

    // Custom comparator for sorting by finish time
    bool operator<(const Activity& other) const {
        return finish < other.finish;
    }
};

std::vector<Activity> activitySelection(std::vector<Activity> activities) {
    if (activities.empty()) {
        return {};
    }

    // Sort activities by finish time (if not already sorted)
    std::sort(activities.begin(), activities.end());

    std::vector<Activity> selected_activities;
    
    // Select the first activity
    selected_activities.push_back(activities[0]);
    int last_finish_time = activities[0].finish;

    // Iterate through the remaining activities
    for (size_t i = 1; i < activities.size(); ++i) {
        const Activity& current_activity = activities[i];

        // If this activity can be selected (doesn't overlap with the last selected one)
        if (current_activity.start >= last_finish_time) {
            selected_activities.push_back(current_activity);
            last_finish_time = current_activity.finish;
        }
    }
            
    return selected_activities;
}

// int main() {
//     std::vector<Activity> activities = {
//         {1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 9}, {5, 9},
//         {6, 10}, {8, 11}, {8, 12}, {2, 14}, {12, 16}
//     };
//     std::vector<Activity> result = activitySelection(activities);
//     for (const auto& act : result) {
//         std::cout << "(" << act.start << ", " << act.finish << ") ";
//     }
//     std::cout << std::endl;
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

type Activity struct {
    Start  int
    Finish int
}

// Implement sort.Interface for []Activity
type ByFinishTime []Activity

func (a ByFinishTime) Len() int           { return len(a) }
func (a ByFinishTime) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByFinishTime) Less(i, j int) bool { return a[i].Finish < a[j].Finish }

func activitySelection(activities []Activity) []Activity {
    if len(activities) == 0 {
        return nil
    }

    // Sort activities by finish time (if not already sorted)
    sort.Sort(ByFinishTime(activities))

    selectedActivities := []Activity{}
    
    // Select the first activity
    selectedActivities = append(selectedActivities, activities[0])
    lastFinishTime := activities[0].Finish

    // Iterate through the remaining activities
    for i := 1; i < len(activities); i++ {
        currentActivity := activities[i]

        // If this activity can be selected (doesn't overlap with the last selected one)
        if currentActivity.Start >= lastFinishTime {
            selectedActivities = append(selectedActivities, currentActivity)
            lastFinishTime = currentActivity.Finish
        }
    }
            
    return selectedActivities
}

// func main() {
//     activities := []Activity{
//         {Start: 1, Finish: 4}, {Start: 3, Finish: 5}, {Start: 0, Finish: 6},
//         {Start: 5, Finish: 7}, {Start: 3, Finish: 9}, {Start: 5, Finish: 9},
//         {Start: 6, Finish: 10}, {Start: 8, Finish: 11}, {Start: 8, Finish: 12},
//         {Start: 2, Finish: 14}, {Start: 12, Finish: 16},
//     }
//     result := activitySelection(activities)
//     for _, act := range result {
//         fmt.Printf("(%d, %d) ", act.Start, act.Finish)
//     }
//     fmt.Println()
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort

// Struct to represent an activity
struct Activity {
    int start;
    int finish;
}

// Custom comparator for sorting by finish time
int compareActivitiesByFinishTime(const Activity a, const Activity b) {
    return a.finish.cmp(b.finish);
}

Activity[] activitySelection(Activity[] activities) {
    if (activities.empty) {
        return [];
    }

    // Sort activities by finish time (if not already sorted)
    activities.sort!compareActivitiesByFinishTime();

    Activity[] selectedActivities;
    
    // Select the first activity
    selectedActivities ~= activities[0];
    int lastFinishTime = activities[0].finish;

    // Iterate through the remaining activities
    foreach (i; 1 .. activities.length) {
        auto currentActivity = activities[i];

        // If this activity can be selected (doesn't overlap with the last selected one)
        if (currentActivity.start >= lastFinishTime) {
            selectedActivities ~= currentActivity;
            lastFinishTime = currentActivity.finish;
        }
    }
            
    return selectedActivities;
}

// void main() {
//     Activity[] activities = [
//         Activity(1, 4), Activity(3, 5), Activity(0, 6), Activity(5, 7),
//         Activity(3, 9), Activity(5, 9), Activity(6, 10), Activity(8, 11),
//         Activity(8, 12), Activity(2, 14), Activity(12, 16)
//     ];
//     auto result = activitySelection(activities);
//     foreach (act; result) {
//         writef("(%d, %d) ", act.start, act.finish);
//     }
//     writeln();
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Activity Selection Problem` demonstrates a simple yet effective greedy strategy. The key is to sort activities by their finish times.

---

**`Activity` Structure:**
- Each `activity` is represented by a `start time` and a `finish time`.

**`activity_selection(activities)` Function:**
- `activities`: A list of `activity` objects/tuples.

**Algorithm Steps:**
- **Sort by Finish Time:** The first crucial step is to sort the input `activities` in non-decreasing order of their `finish times`. This is typically done before calling the `activity_selection` function or as the first step within it. This sorting allows the greedy choice to be made effectively.
- **Initialize:**
- `selected_activities`: An empty list to store the activities chosen for the maximum set.
- If the `activities` list is empty, return an empty list.
- The first `activity` (which has the earliest finish time after sorting) is always selected and added to `selected_activities`.
- `last_finish_time`: Stores the finish time of the most recently selected `activity`. This helps in checking compatibility.

    </li>
- **Iterate and Select:** The algorithm then iterates through the remaining `activities` (from the second activity onwards).
- For each `current_activity`:
- It checks if the `current_activity`'s `start time` is greater than or equal to `last_finish_time`. This condition ensures that the `current_activity` does not overlap with the `activity` that was last selected.
- If the condition is met (the `activities` are compatible):
- The `current_activity` is added to `selected_activities`.
- `last_finish_time` is updated to the `finish time` of the `current_activity`.

                    </li>

            </li>

    </li>

**Result:**
- The `selected_activities` list contains the maximum number of non-overlapping activities that can be performed.

[Back to Implementation](#implementation)

## Applications

### Application

The `Activity Selection Problem` has direct applications in various scheduling and resource allocation scenarios:
- **Meeting Scheduling:** Maximizing the number of meetings that can be scheduled in a conference room without overlaps.
- **Job Scheduling:** Optimizing the number of jobs a single machine or processor can complete within their respective time windows.
- **Resource Allocation:** Allocating a single, limited resource (e.g., a classroom, a car, a piece of equipment) to serve the maximum number of requests/activities.
- **Event Planning:** Scheduling a maximum number of events in a venue where each event has a start and end time.
- **Operating Systems:** CPU scheduling where processes have start and finish times, and the goal is to maximize throughput by selecting non-overlapping processes.

