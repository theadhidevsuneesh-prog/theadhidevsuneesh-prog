-- Pandoc Lua filter: turn  ::: {.def t="Title"}  into a styled callout box with a header chip.
local labels = {
  idea = "Big idea", def = "Definition", thm = "Theorem", formula = "Formula",
  warn = "Watch out", tip = "Exam tip", ex = "Example", try = "Try it",
  story = "Story time", recall = "Quick recall", mem = "Memory trick", proof = "Proof",
}

local function title_inlines(t)
  if t == nil or t == "" then return {} end
  local doc = pandoc.read(t, "markdown+tex_math_dollars")
  local blk = doc.blocks[1]
  if blk and blk.content then return blk.content end
  return {}
end

function Div(el)
  for _, c in ipairs(el.classes) do
    if labels[c] then
      local t = el.attributes["t"]
      local inl = { pandoc.Span(labels[c], { class = "chip" }) }
      if t ~= nil and t ~= "" then
        local ti = title_inlines(t)
        inl[#inl + 1] = pandoc.Span(ti, { class = "bt" })
      end
      local head = pandoc.Div({ pandoc.Plain(inl) }, { class = "bh" })
      table.insert(el.content, 1, head)
      el.classes:insert("box")
      el.attributes["t"] = nil
      return el
    end
  end
  -- solution blocks inside examples
  for _, c in ipairs(el.classes) do
    if c == "sol" then return el end
  end
end
