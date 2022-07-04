# json2bookmarks

`json2bookmarks` helps to convert a bookmarks file in json format
to a html file.

## How it works

Let's take a sample json file,

```json
{
    "items": [
        {
            "title": "google",
            "site": "http://www.google.com",
        },
        {
            "site": "http://web.whatsapp.com"
        }
    ]
}
```

- Notice that the bookmarks are inside `"items"` as a array of object
- Every bookmark can have `"title"`, `"site"`, `"image"`
- If the image is empty when you run the script on the file it will 
  generate a html file and also update you current file with the 
  `favicon` image for the site for the `"image"` key.

# License

[MIT](./LICENSE)