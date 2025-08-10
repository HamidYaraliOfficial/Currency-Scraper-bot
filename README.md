# Currency Scraper

## English

### Overview
Currency Scraper is a tool designed to scrape currency exchange rates from tejaratnews.com. It supports multiple currencies and provides data in JSON format, including prices, changes, and update times. The project includes implementations in both PHP and Python, offering flexibility for different development environments.

### Features
- Scrapes exchange rates for 23 currencies
- Outputs data in JSON format with Unicode support
- Includes flag emojis for each currency
- Handles errors gracefully with detailed error messages
- Provides update timestamps for data freshness

### Requirements
#### PHP Version
- PHP >= 7.4
- Extensions: `curl`, `dom`, `libxml`
- Composer (optional for dependency management)

#### Python Version
- Python >= 3.8
- Packages: `requests`, `beautifulsoup4`
- pip for package installation

### Installation
#### PHP
1. Ensure PHP and required extensions are installed.
2. Copy `CurrencyScraper.php` to your project directory.
3. Run the script using a PHP server or CLI:
   ```bash
   php CurrencyScraper.php
   ```

#### Python
1. Install Python and pip.
2. Install required packages:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Copy `currency_scraper.py` to your project directory.
4. Run the script:
   ```bash
   python currency_scraper.py
   ```

### Usage
#### PHP
Run the script to scrape currency data and output JSON:
```bash
php CurrencyScraper.php
```
The output will be a JSON object containing currency data, update time, and status.

#### Python
Run the script to scrape currency data and output JSON:
```bash
python currency_scraper.py
```
The output will be a JSON object with the same structure as the PHP version.

### Contributing
Contributions are welcome! Please submit pull requests or open issues for bug reports, feature requests, or improvements. Ensure code follows the project's coding style and includes appropriate tests.

### License
This project is licensed under the MIT License.

---

## فارسی

### بررسی اجمالی
اسکریپر ارز ابزاری است که برای جمع‌آوری نرخ‌های ارز از وب‌سایت tejaratnews.com طراحی شده است. این ابزار از چندین ارز پشتیبانی می‌کند و داده‌ها را به فرمت JSON ارائه می‌دهد که شامل قیمت‌ها، تغییرات و زمان به‌روزرسانی است. پروژه شامل پیاده‌سازی‌هایی به زبان‌های PHP و Python است که انعطاف‌پذیری را برای محیط‌های توسعه مختلف فراهم می‌کند.

### ویژگی‌ها
- جمع‌آوری نرخ ارز برای ۲۳ ارز مختلف
- خروجی داده‌ها به فرمت JSON با پشتیبانی از یونیکد
- شامل شکلک‌های پرچم برای هر ارز
- مدیریت خطاها به صورت حرفه‌ای با پیام‌های خطای دقیق
- ارائه زمان به‌روزرسانی برای اطمینان از تازگی داده‌ها

### پیش‌نیازها
#### نسخه PHP
- PHP نسخه ۷.۴ یا بالاتر
- افزونه‌ها: `curl`، `dom`، `libxml`
- Composer (اختیاری برای مدیریت وابستگی‌ها)

#### نسخه Python
- Python نسخه ۳.۸ یا بالاتر
- بسته‌ها: `requests`، `beautifulsoup4`
- pip برای نصب بسته‌ها

### نصب
#### PHP
1. اطمینان حاصل کنید که PHP و افزونه‌های مورد نیاز نصب شده‌اند.
2. فایل `CurrencyScraper.php` را به دایرکتوری پروژه خود کپی کنید.
3. اسکریپت را با استفاده از سرور PHP یا خط فرمان اجرا کنید:
   ```bash
   php CurrencyScraper.php
   ```

#### Python
1. Python و pip را نصب کنید.
2. بسته‌های مورد نیاز را نصب کنید:
   ```bash
   pip install requests beautifulsoup4
   ```
3. فایل `currency_scraper.py` را به دایرکتوری پروژه خود کپی کنید.
4. اسکریپت را اجرا کنید:
   ```bash
   python currency_scraper.py
   ```

### استفاده
#### PHP
اسکریپت را اجرا کنید تا داده‌های ارز جمع‌آوری شده و به فرمت JSON خروجی داده شود:
```bash
php CurrencyScraper.php
```
خروجی یک شیء JSON خواهد بود که شامل داده‌های ارز، زمان به‌روزرسانی و وضعیت است.

#### Python
اسکریپت را اجرا کنید تا داده‌های ارز جمع‌آوری شده و به فرمت JSON خروجی داده شود:
```bash
python currency_scraper.py
```
خروجی یک شیء JSON با همان ساختار نسخه PHP خواهد بود.

### مشارکت
مشارکت‌ها استقبال می‌شوند! لطفاً درخواست‌های pull یا مسائل را برای گزارش باگ، درخواست ویژگی یا بهبود ارسال کنید. اطمینان حاصل کنید که کد از سبک کدنویسی پروژه پیروی می‌کند و شامل تست‌های مناسب است.

### مجوز
این پروژه تحت مجوز MIT منتشر شده است.

---

## 中文

### 概述
货币抓取器是一个用于从 tejaratnews.com 抓取汇率的工具。它支持多种货币，并以 JSON 格式提供数据，包括价格、变化和更新时间。该项目包含 PHP 和 Python 两种实现，为不同的开发环境提供灵活性。

### 功能
- 抓取 23 种货币的汇率
- 以 JSON 格式输出数据，支持 Unicode
- 为每种货币包含国旗表情符号
- 优雅地处理错误，提供详细的错误信息
- 提供更新时间戳以确保数据新鲜度

### 要求
#### PHP 版本
- PHP >= 7.4
- 扩展：`curl`、`dom`、`libxml`
- Composer（可选，用于依赖管理）

#### Python 版本
- Python >= 3.8
- 包：`requests`、`beautifulsoup4`
- pip 用于包安装

### 安装
#### PHP
1. 确保已安装 PHP 及所需扩展。
2. 将 `CurrencyScraper.php` 复制到项目目录。
3. 使用 PHP 服务器或命令行运行脚本：
   ```bash
   php CurrencyScraper.php
   ```

#### Python
1. 安装 Python 和 pip。
2. 安装所需包：
   ```bash
   pip install requests beautifulsoup4
   ```
3. 将 `currency_scraper.py` 复制到项目目录。
4. 运行脚本：
   ```bash
   python currency_scraper.py
   ```

### 使用
#### PHP
运行脚本以抓取货币数据并输出 JSON：
```bash
php CurrencyScraper.php
```
输出将是一个包含货币数据、更新时间和状态的 JSON 对象。

#### Python
运行脚本以抓取货币数据并输出 JSON：
```bash
python currency_scraper.py
```
输出将是一个与 PHP 版本结构相同的 JSON 对象。

### 贡献
欢迎贡献！请提交拉取请求或开设问题以报告错误、请求功能或改进。确保代码遵循项目的编码风格并包含适当的测试。

### 许可证
该项目基于 MIT 许可证发布。