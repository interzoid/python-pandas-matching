# python-pandas-matching
Python code that calls Interzoid's Generative AI-enriched matching APIs to generate similarity keys for organization names (including international), which are then appended to pandas to create match reports.

This is an example of how AI-enhanced similarity keys generated from Interzoid's APIs are used to identify inconsistent yet matching corporate or organization name data, especially with international organization names. Since AI-models are used, this gives us results that go far beyond traditional string matching techniques, including international language characters and languages.

To see some examples of similarity keys with inconsistent data, see this [blog entry](https://blog.interzoid.com/entries/global-org-matching-ai)

To achieve this kind of matching in the code example, we will use Interzoid's Company & Organization Matching API. This is a scalar API, meaning we will call it once for each row we analyze. Since it is a JSON API, it can be used almost anywhere, making it easy to implement in this example.

Functionally, the API will be sent the name of an entity, such as an organization or company name, from each row in a data frame. The API will analyze and process the name using specialized algorithms, knowledge bases, machine learning techniques, and an AI language model. It will respond with a generated similarity key, which is essentially a hashed canonical key encapsulating the many different variations the organization or company name could have within a dataset. This makes it easy to match up names despite differences in their actual electronic, data-described representation. Refer to the aforementioned blog entry to learn more about similarity keys.

Here is the API endpoint we will use to process row values for matching purposes in this example:

```
    url = 'https://api.interzoid.com/getcompanymatchadvanced'
```
                
There are a few Python libraries in this code example. If not already installed in your environment, please install the libraries as follows:

```
    $ pip install pandas
    $ pip install requests
    $ pip install tabulate
```
                
We could just sort the data frame by generated similarity key to get the matching organization names to line up next to each other. However, to make the results more readable and resembling something more like a report, we will add a space between the records of each matching set of similarity keys. Additionally, we will not show the entries where an organization or company name has no other data value that shares the same similarity key. This will ensure that we will only display rows that have matches, enabling us to clearly see the data redundancy that exists in our dataset.

Example output:

```
    ibm inc          edplDLsBWcH9Sa7ZECaJx8KiEl5lvMWAa6ackCA4azs
    IBM              edplDLsBWcH9Sa7ZECaJx8KiEl5lvMWAa6ackCA4azs

    go0gle llc       pGWzK9MrYZzcyOrW5AkpnJYiOgI3qnO0EhwsuNh_dxk
    Google           pGWzK9MrYZzcyOrW5AkpnJYiOgI3qnO0EhwsuNh_dxk

    Microsoft Corp.  xUhcrilUNsRiCthe7rXkIupHiCbhhgyLrKNAcXruwoA
    Microsot         xUhcrilUNsRiCthe7rXkIupHiCbhhgyLrKNAcXruwoA
    microsfttt       xUhcrilUNsRiCthe7rXkIupHiCbhhgyLrKNAcXruwoA
```
