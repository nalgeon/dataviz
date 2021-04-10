cp -r docs/img build
cp docs/epub.css build
cat \
  docs/title.md \
  docs/01-say.md \
  docs/02-structure.md \
  docs/04-express.md \
  docs/05-simplify.md \
  docs/06-condense.md \
  docs/07-check.md \
  docs/09-unify.md \
  docs/epilogue.md \
  > build/data-visualization-guide.md
cd build
sed -E -e 's/docs\///g' -i '' data-visualization-guide.md
sed -E -e 's/^.+(←|→).+$/ /g' -i '' data-visualization-guide.md
sed -E -e 's/[0-9]+-[a-z]+\.md//g' -i '' data-visualization-guide.md