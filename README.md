# Bookmarkino
Simple program to save your bookmarks separate from the browser.

## How to use it
Just typing `bookmarkino` or `bookmarkino -h` will lead you to help menu.

Basically there is a sqlite database and Bookmarkino saves bookmarks in it and lists you if you want.

To insert a new bookmark run `bookmarkino -i https://your-desired-bookmark-address`. To list saved bookmarks run `bookmarkino -l`.

## Roadmap
With Bookmarkino I want to have minimum features and maximum usability.
- [ ] Delete bookmarks
- [ ] Grouping or foldering bookmarks
- [ ] Import bookmarks from Chrome and Firefox
- [ ] Self hostable server for sync
- [ ] Browser extension?
- [ ] Mobile app

## Contributing
Feel free to play with it. There is no guideline available (yet) and Berkay may not accept your PR :^)

## Testing
To keep things simple, Bookmarkino is using built-in unittest library. Type `make run_test` to run all available tests.
