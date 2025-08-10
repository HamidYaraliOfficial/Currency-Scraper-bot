<?php
declare(strict_types=1);
namespace CurrencyScraper;
use DOMDocument;
use DOMXPath;
use RuntimeException;
header('Content-Type: application/json; charset=utf-8');
final class CurrencyScraper
{
    private const BASE_URL = 'https://tejaratnews.com/';
    private const CURRENCIES = [
        'دلار' => ['path' => 'قیمت-دلار', 'flag' => '🇺🇸'],
        'یورو' => ['path' => 'قیمت-یورو', 'flag' => '🇪🇺'],
        'پوند' => ['path' => 'قیمت-پوند', 'flag' => '🇬🇧'],
        'درهم امارات' => ['path' => 'قیمت-درهم-امارات', 'flag' => '🇦🇪'],
        'لیر ترکیه' => ['path' => 'قیمت-لیر-ترکیه', 'flag' => '🇹🇷'],
        'یوان چین' => ['path' => 'قیمت-یوان-چین', 'flag' => '🇨🇳'],
        'روبل روسیه' => ['path' => 'قیمت-روبل-روسیه', 'flag' => '🇷🇺'],
        'دینار عراق' => ['path' => 'قیمت-دینار-عراق', 'flag' => '🇮🇶'],
        'دلار کانادا' => ['path' => 'قیمت-دلار-کانادا', 'flag' => '🇨🇦'],
        'افغانی افغانستان' => ['path' => 'قیمت-افغانی-افغانستان', 'flag' => '🇦🇫'],
        'ریال قطر' => ['path' => 'قیمت-ریال-قطر', 'flag' => '🇶🇦'],
        'ریال عمان' => ['path' => 'قیمت-ریال-عمان', 'flag' => '🇴🇲'],
        'دلار استرالیا' => ['path' => 'قیمت-دلار-استرالیا', 'flag' => '🇦🇺'],
        'کرون سوئد' => ['path' => 'قیمت-کرون-سوئد', 'flag' => '🇸🇪'],
        'درام ارمنستان' => ['path' => 'قیمت-درام-ارمنستان', 'flag' => '🇦🇲'],
        'منات آذربایجان' => ['path' => 'قیمت-منات-اذربایجان', 'flag' => '🇦🇿'],
        'فرانک سوئیس' => ['path' => 'قیمت-فرانک-سوئیس', 'flag' => '🇨🇭'],
        'کرون دانمارک' => ['path' => 'قیمت-کرون-دانمارک', 'flag' => '🇩🇰'],
        'روپیه هند' => ['path' => 'قیمت-روپیه-هند', 'flag' => '🇮🇳'],
        'رینگیت مالزی' => ['path' => 'قیمت-رینگیت-مالزی', 'flag' => '🇲🇾'],
        'کرون نروژ' => ['path' => 'قیمت-کرون-نروژ', 'flag' => '🇳🇴'],
        'ریال عربستان' => ['path' => 'قیمت-ریال-عربستان', 'flag' => '🇸🇦'],
        'دلار سنگاپور' => ['path' => 'قیمت-دلار-سنگاپور', 'flag' => '🇸🇬'],
    ];
    private function fetchHtml(string $url): string
    {
        $ch = curl_init($url);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_TIMEOUT => 30,
        ]);
        $html = curl_exec($ch);
        if ($html === false) {
            throw new RuntimeException('Failed to fetch HTML from ' . $url);
        }
        curl_close($ch);
        return $html;
    }
    private function parsePrice(string $html, string $currencyName): array
    {
        $dom = new DOMDocument();
        @$dom->loadHTML('<?xml encoding="utf-8" ?>' . $html);
        $xpath = new DOMXPath($dom);
        $data = [];
        $unit = 'تومان';
        $date = null;
        $dateNodes = $xpath->query('//tfoot/tr/td');
        if ($dateNodes->length > 0 && preg_match('/تاریخ بروزرسانی:\s*([\d\/]+)/u', $dateNodes[0]->textContent, $matches)) {
            $date = $matches[1];
        }
        foreach ($xpath->query('//table/tbody/tr') as $row) {
            $cols = $row->getElementsByTagName('td');
            if ($cols->length < 4) {
                continue;
            }
            $name = trim($cols->item(0)->textContent);
            if ($name !== $currencyName) {
                continue;
            }
            $data[] = [
                'name' => $name,
                'price' => (int) str_replace(',', '', $cols->item(1)->textContent),
                'change' => trim($cols->item(2)->textContent),
                'time' => trim($cols->item(3)->textContent),
            ];
        }
        return compact('unit', 'date', 'data');
    }
    public function scrape(): array
    {
        $result = [];
        foreach (self::CURRENCIES as $name => $config) {
            try {
                $result[$name] = array_merge(
                    $this->parsePrice($this->fetchHtml(self::BASE_URL . $config['path']), $name),
                    ['flag' => $config['flag']]
                );
            } catch (RuntimeException $e) {
                $result[$name] = ['error' => 'خطا در دریافت داده‌ها: ' . $e->getMessage(), 'flag' => $config['flag']];
            }
        }
        return [
            'ok' => true,
            'updated' => date('Y-m-d H:i:s'),
            'currencies' => $result,
        ];
    }
}
try {
    $scraper = new CurrencyScraper();
    echo json_encode($scraper->scrape(), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'سرور با خطا مواجه شد'], JSON_UNESCAPED_UNICODE);
}
?>