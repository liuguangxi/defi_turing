#import "../templates/preamble.typ": *


#page(
  paper: "a4",
)[
  #set text(font: sans-font)
  #v(8em)
  #text(size: 36pt)[
    #text(fill: main-color)[*Défi Turing*]
  ]
  #v(-2em)
  #text(size: 36pt)[
    *Unofficial Offline Edition*
  ]
  #v(0em)
  #text(size: 24pt)[
    #text(fill: sec-color)[English Version]
  ]
  #align(right + bottom)[
    #text(size: 16pt)[
      Revision #text(fill: main-color)[*v2025.1*]
    ]
  ]
  #pagebreak(weak: true)
]
