
## setup environment (as outlined in `README.md`)

Using `pyenv` with python 3.12.

```bash
make up
```

## modifed seed

Modified seed to include extra column for text so we can do a better demo and not insert the 50K demo records without text.
All code generated using `opencode` with `Gemini 3.1 Flash Lite Preview`.

```bash
make seed
```

## created `insert.py` to insert text records for testing (modified table to include `content`)

Using other random variables as layed out in `data/seed.py` (perhaps improvement here is to use extra parameters for inserting structured values like `juristiction` and `practice_area`.

```bash
python insert.py "Rock test 1234"
python insert.py "Rock test 4321"
```

## search for vector text in db using text

### first search with filter and text, as required

```bash
python3 search_with_filter.py "Rock test 1234" --practice_area tax --jurisdiction AU
```

Top 5 matches for: Rock test 1234 (Jurisdiction: AU, Area: tax (both randomly generated values))

| Score | Content |
| ----  | ------- |
| 0.8824 | Rock test 4321 |


### secondly without filter

```bash
python3 text_search.py "Rock test 1234"
```

Top 5 matches for: Rock test 1234

| Score | Content |
| ----- | ------- |
| 1.0 | Rock test 1234 |
| 0.8824 | Rock test 4321 |




