# project notes

## Install the tools

```bash
pip install django scrapy scrapyd
```

## Create a django project

Here, we named it `hotel`

```bash
django-admin startproject hotel
```

## Create a scrapy project and generate a spider

```bash
cd hotel
scrapy startproject hotel_spider
cd hotel_spider
scrapy genspider github github.com
```

## Install the scrapyd and update setting

```bash
cd hotel_spider
touch scrapyd.conf
```
scrapyd.conf
```config
[scrapyd]
bind_address = 0.0.0.0
```

## Run a spider
```bash
cd hotel_spider
scrapyd
```

## Call the spider api

- make a request job

```bash
curl http://localhost:6800/schedule.json -d project=default -d spider=github
```
  - pass the parameters
  ```bash
  curl http://localhost:6800/schedule.json -d project=default -d spider=ctrip -d 'urls=https://ctrip.com/1/,https://baidu.com/1'
  ```

- get the job result

```bash
curl 'http://localhost:6800/listjobs.json?project=default'
```

## use cookie

[scrapy中如何设置应用cookies](https://blog.csdn.net/fuck487/article/details/84617194)
