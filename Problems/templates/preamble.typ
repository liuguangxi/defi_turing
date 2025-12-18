#let serif-font = "Minion Pro"
#let sans-font = "Myriad Pro"
#let mono-font = "Consolas"

#let main-color = rgb("#ff2a00").darken(25%)
#let sec-color = rgb("#0019ff").darken(50%)


#let init(body) = {
  set page(
    paper: "a4",
    header: [
      #set align(center)
      #box(width: 1fr, inset: (y: 5pt), stroke: (bottom: luma(50%) + 0.75pt))[
        #text(font: serif-font, size: 11pt)[#smallcaps[Défi Turing Offline]]
      ]
      #counter(footnote).update(0)
    ],
    footer: [
      #set align(center)
      #text(font: serif-font, size: 11pt, number-type: "old-style")[
        Page #context counter(page).display("1 of 1", both: true)
      ]
    ]
  )

  counter(page).update(1)

  set par(justify: true)
  set text(font: serif-font, size: 11pt)
  show raw: set text(font: mono-font, size: 10pt)

  set list(indent: 1em)
  set enum(indent: 1em)

  show footnote: set text(fill: sec-color)
  show ref: set text(fill: sec-color)
  show link: set text(fill: sec-color, weight: "bold")

  // Main body
  body
}


#let problem-block(number: none, title: none, bm-title: none, body) = {
  [
    #let bookmark-title = if bm-title == none {
      [Problem \##number: #title]
    } else {
      [Problem \##number: #bm-title]
    }
    #set text(size: 0pt)
    #heading(hide[#bookmark-title])
    #label("p" + str(number))
  ]

  [
    #set text(font: sans-font, size: 14.5pt, fill: sec-color)
    #if number != none [#text(fill: main-color)[*#number* #h(4pt)]]
    #box(baseline: 7pt, fill: luma(50%), width: 2.5pt, height: 25pt)
    #h(4pt) *#title*
    #parbreak()
  ]

  body
  pagebreak(weak: true)
}
