# Sklearn image package for workshop

## Steps

1. `cd` into `src/`
2. Build image using the Dockerfile
3. Use image in corresponding Lambda session

## Test

Use the following JSON schema:

```json
{
	"body": {
	    "features": {
		"sepal length (cm)": 6.4,
		"sepal width": 2.9,
		"petal length": 4.3,
		"petal width": 1.3
	    }
	}
}
```