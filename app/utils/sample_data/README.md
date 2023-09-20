# How to get data:

There are three endpoints
- deltager
- produktionsenhed
- virksomhed

## Api url
GET http://distribution.virk.dk/cvr-permanent/{endpoint}/_search?scroll=5m

Basic Auth with username and password

Content-Type: application/json

should for OR
must for AND

```JSON
{ 
	"query": {
		"bool": {
			"should": [
				{
					"range": {
						"Vrvirksomhed.virksomhedMetadata.nyesteNavn.sidstOpdateret": {
							"gte": "2023-06-10T20:45:00"}
						}
				},
				{
					"range": {
						"Vrvirksomhed.maanedsbeskaeftigelse.sidstOpdateret": 
							{"gte": "2023-06-10T20:45:00"}
						}
				}       
			]
		}
  	},
  "size": 1
}
```