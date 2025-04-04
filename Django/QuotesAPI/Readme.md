# Quotes API
## Introduction
  The Quotes API is a versatile tool build in Django that provides access to a vast collection of inspirational, motivational, and thought-provoking quotes. Whether you're building an application, website, or project, this API allows you to effortlessly integrate inspiring quotes into your content, enriching user experiences.

## Features
  - Extensive Database: The API offers a comprehensive collection of quotes from various categories, ensuring you find the perfect quote for your needs.
  - Random Quote Generation: Surprise and inspire users with random quotes, perfect for applications that seek to deliver fresh content.
  - Author Attribution: Each quote includes the author, enabling proper attribution for the wisdom and insights shared.
  - API Integration: The Quotes API provides a straightforward HTTP interface for seamless integration into various platforms and programming languages.
  - Open Access: The API is open and accessible to everyone, without complex authentication requirements, making it ideal for hobbyists, educational projects, and developers at all levels.

## Usage
<p>To use the Random Jokes API, you can make a GET request to the provided endpoint `JokesAPI` to retrieve a random joke in JSON format.</p>
  Use the Quotes API by making simple HTTP requests to the API endpoints to retrieve quotes that align with your project's goals. This versatility allows you to easily integrate inspirational quotes into mobile apps, websites, scripts, and more.

### Example in JS
 Here's an example of how to use the Quotes API to fetch a random quote in JS:

```JavaScript
fetch("GET","https://quotesapi.santosh0.com.np/api/quotes/")
.then(response=>response.json())
.then(response=>{
    console.log(response);
}).catch(e=>{
    console.log(e);
})
```
### Example in Python
  Here's an example of how to use the Quotes API to fetch a random quote in Python:

```python
import requests

url = "https://quotesapi.santosh0.com.np/api/quotes/"
response = requests.get(url)
data = response.json()

print(f"Random Quote: {data['quotes']} - {data['author']}")
```
### Example in Java
  Here's an example of how to use the Quotes API to fetch a random quote in Java:

```java
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.ResponseBody;
import org.json.JSONObject;

public class QuotesApiClient {
    public static void main(String[] args) {
        OkHttpClient client = new OkHttpClient();
        String apiUrl = "https://quotesapi.santosh0.com.np/api/quotes/"; 

        Request request = new Request.Builder()
            .url(apiUrl)
            .get()
            .build();

        try {
            Response response = client.newCall(request).execute();
            if (response.isSuccessful()) {
                ResponseBody responseBody = response.body();
                if (responseBody != null) {
                    String jsonData = responseBody.string();
                    JSONObject json = new JSONObject(jsonData);
                    String quote = json.getString("auotesd");
                    String author = json.getString("author");
                    System.out.println("Random Quote: " + quote + " - " + author);
                }
            } else {
                System.out.println("Error: " + response.code() + " - " + response.message());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

### Example Response

```json
{ 
    "quotes": "If you want to live a happy life, tie it to a goal, not to people or things.", 
    "author": "Albert Einstein" 
}
```

## Conclusion
The Quotes API provides a simple and fun way to generate Quotes. Feel free to use it in your projects or contribute to its development. We appreciate your support and welcome any feedback or suggestions. Enjoy the laughter!

## Contributing

We welcome contributions! If you'd like to contribute to this project, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct

Please review our [Code of Conduct](CodeOfConduct.md) before participating in this project.

## License

This project is licensed under the MIT [License](LICENSE).