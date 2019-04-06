# project_douban

a spider of [douban's top 250 movies]([www.douban.com/top250](https://movie.douban.com/top250)) using scrapy

also there is a commit using scrapy redis (although for this project, scrapy is enough)

using below command to run the spider (need to install scrapy first)

```bash
scrapy crawl douban -o douban.json
```