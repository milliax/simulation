\ Model The name
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0x6e8f6d7e3860a76b
Minimize
  3 workers[A] + 2 workers[B] + workers[C] + 2 workers[D]
Subject To
 cover_1: workers[A] >= 1
 cover_2: workers[A] + workers[B] >= 1
 cover_3: workers[B] + workers[C] >= 1
 cover_4: workers[C] + workers[D] >= 1
Bounds
Binaries
 workers[A] workers[B] workers[C] workers[D]
End
