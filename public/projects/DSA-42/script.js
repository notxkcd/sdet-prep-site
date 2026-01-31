document.addEventListener('DOMContentLoaded', () => {
    const homeScreen = document.getElementById('home-screen');
    const contentScreen = document.getElementById('content-screen');
    const dsFundamentalsList = document.getElementById('ds-fundamentals-list');
    const dsSpecializedList = document.getElementById('ds-specialized-list');
    const algoList = document.getElementById('algo-list');
    const contentTitle = document.getElementById('content-title');
    const contentExplanation = document.getElementById('content-explanation');
    const contentExpandedExplanation = document.getElementById('content-expanded-explanation');
    const languageSelector = document.getElementById('language-selector');
    const codeDisplay = document.getElementById('code-display');
    const codeExplanation = document.getElementById('code-explanation');
    const applicationContent = document.getElementById('application-content');
    const backButton = document.getElementById('back_button');
    const copyButton = document.getElementById('copy-button');

    // --- DATA ---
    const contentData = {
        dataStructures: {
            fundamentals: [
                { title: 'Array / Dynamic Array', filePath: 'content/data_structures/fundamentals/array.html' },
                { title: 'Linked List', filePath: 'content/data_structures/fundamentals/linked_list.html' },
                { title: 'Stack', filePath: 'content/data_structures/fundamentals/stack.html' },
                { title: 'Queue', filePath: 'content/data_structures/fundamentals/queue.html' },
                { title: 'Hash Table', filePath: 'content/data_structures/fundamentals/hash_table.html' },
                { title: 'Set', filePath: 'content/data_structures/fundamentals/set.html' },
                { title: 'Heap', filePath: 'content/data_structures/fundamentals/heap.html' },
                { title: 'Binary Search Tree', filePath: 'content/data_structures/fundamentals/binary_search_tree.html' },
                { title: 'Graph', filePath: 'content/data_structures/fundamentals/graph.html' }
            ],
            specialized: [
                { title: 'Trie', filePath: 'content/data_structures/specialized/trie.html' },
                { title: 'Splay Tree', filePath: 'content/data_structures/specialized/splay_tree.html' },
                { title: 'AVL Tree', filePath: 'content/data_structures/specialized/avl_tree.html' },
                { title: 'Red-Black Tree', filePath: 'content/data_structures/specialized/red_black_tree.html' },
                { title: 'Treap', filePath: 'content/data_structures/specialized/treap.html' },
                { title: 'Scapegoat Tree', filePath: 'content/data_structures/specialized/scapegoat_tree.html' },
                { title: 'K-D Tree', filePath: 'content/data_structures/specialized/k_d_tree.html' },
                { title: 'Quadtree', filePath: 'content/data_structures/specialized/quadtree.html' },
                { title: 'Octree', filePath: 'content/data_structures/specialized/octree.html' },
                { title: 'Interval Tree', filePath: 'content/data_structures/specialized/interval_tree.html' },
                { title: 'Metric Tree', filePath: 'content/data_structures/specialized/metric_tree.html' },
                { title: 'R-Tree', filePath: 'content/data_structures/specialized/r_tree.html' },
                { title: 'B-Tree', filePath: 'content/data_structures/specialized/b_tree.html' },
                { title: 'B+ Tree', filePath: 'content/data_structures/specialized/b_plus_tree.html' },
                { title: 'Skip List', filePath: 'content/data_structures/specialized/skip_list.html' },
                { title: 'Segment Tree', filePath: 'content/data_structures/specialized/segment_tree.html' },
                { title: 'Segment Tree with Lazy Propagation', filePath: 'content/data_structures/specialized/segment_tree_lazy.html' },
                { title: 'Fenwick Tree', filePath: 'content/data_structures/specialized/fenwick_tree.html' },
                { title: 'Disjoint Set Union', filePath: 'content/data_structures/specialized/disjoint_set_union.html' },
                { title: 'Fibonacci Heap', filePath: 'content/data_structures/specialized/fibonacci_heap.html' },
                { title: 'Leftist Heap', filePath: 'content/data_structures/specialized/leftist_heap.html' },
                { title: 'Skew Heap', filePath: 'content/data_structures/specialized/skew_heap.html' },
                { title: 'Pairing Heap', filePath: 'content/data_structures/specialized/pairing_heap.html' },
                { title: 'Binomial Heap', filePath: 'content/data_structures/specialized/binomial_heap.html' },
                { title: 'Suffix Array', filePath: 'content/data_structures/specialized/suffix_array.html' },
                { title: 'Suffix Tree', filePath: 'content/data_structures/specialized/suffix_tree.html' },
                { title: 'Suffix Automaton', filePath: 'content/data_structures/specialized/suffix_automaton.html' },
                { title: 'Bloom Filter', filePath: 'content/data_structures/specialized/bloom_filter.html' },
                { title: 'Count-Min Sketch', filePath: 'content/data_structures/specialized/count_min_sketch.html' },
                { title: 'CRDT', filePath: 'content/data_structures/specialized/crdt.html' },
                { title: 'HyperLogLog', filePath: 'content/data_structures/specialized/hyperloglog.html' },
                { title: 'Van Emde Boas Tree', filePath: 'content/data_structures/specialized/van_emde_boas_tree.html' },
                { title: 'Wavelet Tree', filePath: 'content/data_structures/specialized/wavelet_tree.html' },
                { title: 'Dancing Links (DLX)', filePath: 'content/data_structures/specialized/dancing_links.html' }
            ]
        },
        algorithms: {
            "Sorting & Searching": [
                { title: 'Binary Search', filePath: 'content/algorithms/sorting_searching/binary_search.html' },
                { title: 'Bubble Sort', filePath: 'content/algorithms/sorting_searching/bubble_sort.html' },
                { title: 'Selection Sort', filePath: 'content/algorithms/sorting_searching/selection_sort.html' },
                { title: 'Insertion Sort', filePath: 'content/algorithms/sorting_searching/insertion_sort.html' },
                { title: 'Merge Sort', filePath: 'content/algorithms/sorting_searching/merge_sort.html' },
                { title: 'Quick Sort', filePath: 'content/algorithms/sorting_searching/quick_sort.html' },
                { title: 'Heap Sort', filePath: 'content/algorithms/sorting_searching/heap_sort.html' },
                { title: 'Radix Sort', filePath: 'content/algorithms/sorting_searching/radix_sort.html' }
            ],
            "Graph Traversal": [
                { title: 'Breadth-First Search (BFS)', filePath: 'content/algorithms/graph_traversal/bfs.html' },
                { title: 'Depth-First Search (DFS)', filePath: 'content/algorithms/graph_traversal/dfs.html' },
                { title: "Dijkstra's Algorithm", filePath: 'content/algorithms/graph_traversal/dijkstra.html' },
                { title: 'A* Search', filePath: 'content/algorithms/graph_traversal/a_star.html' },
                { title: 'Topological Sort', filePath: 'content/algorithms/graph_traversal/topological_sort.html' }
            ],
            "String Search Algorithms": [
                { title: 'Knuth-Morris-Pratt (KMP)', filePath: 'content/algorithms/string_searching/kmp.html' },
                { title: 'Rabin-Karp Algorithm', filePath: 'content/algorithms/string_searching/rabin_karp.html' },
                { title: 'Z-Algorithm', filePath: 'content/algorithms/string_searching/z_algorithm.html' },
                { title: 'Boyer-Moore Algorithm', filePath: 'content/algorithms/string_searching/boyer_moore.html' }
            ],
            "Dynamic Programming": [
                { title: 'Longest Common Subsequence (LCS)', filePath: 'content/algorithms/dynamic_programming/lcs.html' },
                { title: 'Edit Distance (Levenshtein Distance)', filePath: 'content/algorithms/dynamic_programming/edit_distance.html' },
                { title: 'Knapsack Problem (0/1 Knapsack)', filePath: 'content/algorithms/dynamic_programming/knapsack.html' },
                { title: 'Matrix Chain Multiplication', filePath: 'content/algorithms/dynamic_programming/matrix_chain_multiplication.html' },
                { title: 'Coin Change Problem (Minimum Coins)', filePath: 'content/algorithms/dynamic_programming/coin_change.html' },
                { title: 'Longest Common Substring', filePath: 'content/algorithms/dynamic_programming/lcs_substring.html' },
                { title: 'Longest Palindromic Subsequence', filePath: 'content/algorithms/dynamic_programming/lps.html' },
                { title: 'Rod Cutting Problem', filePath: 'content/algorithms/dynamic_programming/rod_cutting.html' }
            ],
            "Graph Algorithms (Shortest Paths / MST)": [
                { title: 'Floyd-Warshall Algorithm', filePath: 'content/algorithms/graph_shortest_paths_mst/floyd_warshall.html' },
                { title: "Prim's Algorithm", filePath: 'content/algorithms/graph_shortest_paths_mst/prim.html' },
                { title: "Kruskal's Algorithm", filePath: 'content/algorithms/graph_shortest_paths_mst/kruskal.html' },
                { title: "Bellman-Ford Algorithm", filePath: 'content/algorithms/graph_shortest_paths_mst/bellman_ford.html' },
                { title: "Boruvka's Algorithm", filePath: 'content/algorithms/graph_shortest_paths_mst/boruvka.html' }
            ],
            "Graph Algorithms (Flow)": [
                { title: 'Ford-Fulkerson Algorithm', filePath: 'content/algorithms/graph_flow/ford_fulkerson.html' },
                { title: 'Edmonds-Karp Algorithm', filePath: 'content/algorithms/graph_flow/edmonds_karp.html' }
            ],
            "Greedy Algorithms": [
                { title: 'Activity Selection Problem', filePath: 'content/algorithms/greedy/activity_selection.html' },
                { title: 'Fractional Knapsack Problem', filePath: 'content/algorithms/greedy/fractional_knapsack.html' },
                { title: 'Huffman Coding Algorithm', filePath: 'content/algorithms/greedy/huffman_coding.html' },
                { title: 'Job Sequencing Problem with Deadlines', filePath: 'content/algorithms/greedy/job_sequencing.html' },
                { title: 'Minimum Platforms Problem', filePath: 'content/algorithms/greedy/min_platforms.html' }
            ],
            "Backtracking Algorithms": [
                { title: 'N-Queens Problem', filePath: 'content/algorithms/backtracking/n_queens.html' },
                { title: 'Sudoku Solver', filePath: 'content/algorithms/backtracking/sudoku_solver.html' }
            ],
            "Divide and Conquer Algorithms": [
                { title: 'Closest Pair of Points', filePath: 'content/algorithms/divide_and_conquer/closest_pair.html' },
                { title: 'Karatsuba Algorithm', filePath: 'content/algorithms/divide_and_conquer/karatsuba.html' }
            ],
            "Number Theory": [
                { title: 'Euclidean Algorithm', filePath: 'content/algorithms/number_theory/euclidean_algorithm.html' }
            ],
            "Miscellaneous Algorithms": [
                { title: 'Fisher-Yates Shuffle', filePath: 'content/algorithms/misc/fisher_yates_shuffle.html' },
                { title: 'Reservoir Sampling', filePath: 'content/algorithms/misc/reservoir_sampling.html' }
            ]
        }
    };

    // --- FUNCTIONS ---

    function populateLists() {
        dsFundamentalsList.innerHTML = '';
        dsSpecializedList.innerHTML = '';
        algoList.innerHTML = '';

        let totalCounter = 1;

        contentData.dataStructures.fundamentals.forEach((item, index) => {
            const li = document.createElement('li');
            li.innerHTML = `<button class="item-button" data-type="ds" data-category="fundamentals" data-index="${index}">${totalCounter}. ${item.title}</button>`;
            dsFundamentalsList.appendChild(li);
            totalCounter++;
        });

        contentData.dataStructures.specialized.forEach((item, index) => {
            const li = document.createElement('li');
            li.innerHTML = `<button class="item-button" data-type="ds" data-category="specialized" data-index="${index}">${totalCounter}. ${item.title}</button>`;
            dsSpecializedList.appendChild(li);
            totalCounter++;
        });

        // Reset counter for algorithms or continue, depending on desired numbering
        let algoCounter = 1; 
        for (const category in contentData.algorithms) {
            const categoryH3 = document.createElement('h3');
            categoryH3.textContent = category;
            algoList.appendChild(categoryH3);

            const categoryUl = document.createElement('ul');
            contentData.algorithms[category].forEach((item, index) => {
                const li = document.createElement('li');
                li.innerHTML = `<button class="item-button" data-type="algo" data-category="${category}" data-index="${index}">${algoCounter}. ${item.title}</button>`;
                categoryUl.appendChild(li);
                algoCounter++;
            });
            algoList.appendChild(categoryUl);
        }
    }

    async function showContent(type, category, index) {
        let item;
        if (type === 'ds') {
            item = contentData.dataStructures[category][index];
        } else if (type === 'algo') {
            item = contentData.algorithms[category][index];
        } else {
            return; // Unknown type
        }

        contentTitle.textContent = item.title;

        try {
            const response = await fetch(item.filePath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const htmlContent = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlContent, 'text/html');

            contentExplanation.innerHTML = doc.getElementById('explanation-content')?.innerHTML || 'Explanation not found.';
            contentExpandedExplanation.innerHTML = doc.getElementById('expanded-explanation-content')?.innerHTML || '';
            codeExplanation.innerHTML = doc.getElementById('code-explanation-content')?.innerHTML || '';
            applicationContent.innerHTML = doc.getElementById('application-content')?.innerHTML || '';
            
            const codeImplementations = doc.getElementById('code-implementations');
            if (codeImplementations) {
                const codeBlocks = codeImplementations.querySelectorAll('pre[data-lang]');
                
                languageSelector.innerHTML = '';
                const implementations = {};
                
                const langOrder = ['python', 'javascript', 'typescript', 'cpp', 'd', 'go'];
                
                // Add languages to the implementations object
                codeBlocks.forEach(block => {
                    const lang = block.getAttribute('data-lang');
                    if (lang) {
                        implementations[lang] = block.querySelector('code').textContent;
                    }
                });

                // Add options to the selector in the desired order
                langOrder.forEach(lang => {
                    if (implementations[lang]) {
                        const option = document.createElement('option');
                        option.value = lang;
                        option.textContent = lang.charAt(0).toUpperCase() + lang.slice(1);
                        languageSelector.appendChild(option);
                    }
                });
                
                languageSelector.onchange = () => {
                    const selectedLang = languageSelector.value;
                    codeDisplay.textContent = implementations[selectedLang];
                    // Important: Set the class for Prism.js
                    codeDisplay.className = `language-${selectedLang}`;
                    Prism.highlightElement(codeDisplay);
                };
                
                languageSelector.dispatchEvent(new Event('change'));
            }

        } catch (error) {
            contentExplanation.innerHTML = `<p class="error-message">Error loading content: ${error}</p>`;
            contentExpandedExplanation.innerHTML = '';
            codeExplanation.innerHTML = '';
            applicationContent.innerHTML = '';
            codeDisplay.textContent = '';
        }

        homeScreen.classList.add('hidden');
        contentScreen.classList.remove('hidden');
    }

    function showHomeScreen() {
        contentScreen.classList.add('hidden');
        homeScreen.classList.remove('hidden');
    }

    // --- EVENT LISTENERS ---
    
    // Note: A real back button would likely be part of index.html, not dynamically created.
    // This assumes a 'back-button' element exists.
    const backButtonElem = document.getElementById('back-button');
    if (backButtonElem) {
        backButtonElem.addEventListener('click', showHomeScreen);
    }

    if (copyButton) {
        copyButton.addEventListener('click', () => {
            const codeToCopy = codeDisplay.textContent;
            navigator.clipboard.writeText(codeToCopy).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = 'Copy';
                }, 2000);
            }, (err) => {
                copyButton.textContent = 'Error';
                console.error('Could not copy text: ', err);
            });
        });
    }
    
    document.addEventListener('click', (e) => {
        const target = e.target;
        if (target && target.classList.contains('item-button')) {
            const type = target.getAttribute('data-type');
            const category = target.getAttribute('data-category');
            const index = target.getAttribute('data-index');
            if(type && category && index !== null) {
                showContent(type, category, parseInt(index, 10));
            }
        }
    });

    // --- INITIALIZATION ---
    populateLists();
});