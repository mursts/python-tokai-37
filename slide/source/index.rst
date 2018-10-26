=====================================================
Python x Google App Engine
=====================================================

| Python東海 x Unagi.py 合同勉強会
| 2018.10.27
| @mursts

お前誰よ
=============================================

**三浦 智 (@mursts)**

* Python東海 管理人の1人
* Python Boot Camp

  * 愛知 現地スタッフ
  * 静岡 TA

* GCPUG Nagoya オーガナイザー


.. image::
   /_static/images/comunity.jpg


今日話すこと
==============================

Google App Engineについて

  デモしながらApp Engineの特徴をお伝えします


動機
==============================

私の観測している範囲では「Herokuで動かしてみた」が多いので、
Webアプリを作った時にApp Engineを使う人が増えてほしい


なぜApp Engine(PaaS)
==============================


Webアプリはどの環境で動かしていますか？
========================================

* 自宅サーバ、Raspberry Pi
* VPS
* クラウドサービス

  * GCP、AWS、Azure、Heroku ...


Webアプリって作るだけじゃないですよね
=====================================

どれを使おう

- uWSGI
- gunicorn
- mod_wsgi
- Nginx Unit

本番環境で Flaskの ``python main.py`` とか Djangoの ``python manage.py runserver`` で動かしませんよね？あくまでも開発用


Webアプリって作るだけじゃないですよね
=====================================

Webサーバはいる？

- Nginx
- Apache
- IIS

  ``nginx.conf`` や ``httpd.conf`` 設定できますか？

.. rst-class:: presenter-notes

 Web Server Gateway Inerface -> PythonとAPサーバをつなぐ仕様


突然来る(とうれしい場合もある)大量アクセス
==========================================

- Internal Server Error
- Service Temporarily Unavailable

  ボトルネックはどこ？ CPU？メモリ？ディスク？


そんな時はPaaSの出番
==============================

できないものはやってもらう

アプリを作るだけに集中したい


Google App Engine
==============================


Google App Engine
==============================

Google App Engine(GAE)とはGoogleが提供するPaasでGCPのサービスの1つ

開発者はアプリケーションを作ることに専念できる

.. image:: /_static/images/appengine.png


Google App Engine
==============================

- コンテナ上でアプリケーションが動く
- リクエストが発生するとインスタンスを起動して、なくなればインスタンスも落ちる

.. rst-class:: presenter-notes

 Borgの話→Kubernetes


Google App Engine
==============================

現在App Engineには3つのタイプが存在する

- Starndard Environment

  - First Generation
  - Second Generation (Beta)

- Frexible Environment <- 今日は触れません


Standard Environment
==============================

First Generation (昔からあるやつ)

- Python 2.7、Java 7、PHP 5.5、Go 1.6 〜 1.9
- ローカルファイルアクセス不可
- 外部リクエストは専用APIを使用（requestsはパッチを当てないと）
- メール送受信
- 画像API

  - Google Cloud Storageにある画像を扱う
  - URLに引数をサイズを指定するだけでリサイズしてくれる
  

Standard Environment
==============================

Second Generation(Beta)

- `gVisor <https://github.com/google/gvisor>`_ ベースのコンテナ
- Python 3.7、Java 8、PHP 7.2、Node.js 8、Go 1.11
- `/tmp` 以下にファイルを保存できる
- 外部リクエストは自由
- `scikit-learnが動く <https://medium.com/google-cloud-jp/gae-standard-with-scikit-learn-dff5ad1a0ea>`_


Frexible Environment
==============================

GAE環境でコンテナを動かせる


App Engineの特徴
==============================


高速スピンアップ
==============================

- Go：30ms
- Python、PHP：300ms
- Java：3000ms

.. rst-class:: presenter-notes

 StackDriverのログ


オートスケーリング
==============================

- アクセスがくるとコンテナを起動する
- アクセス数に応じて起動するコンテナの数を制御

  - みんなが寝てる時間はコンテナは落ちている

.. rst-class:: presenter-notes

 画像を見せる
 ヒルナンデス


料金
==============================

- 毎月の無料枠がある 
- アクセスが無ければ料金は発生しない

.. rst-class:: presenter-notes

 一日5000件のアクセスで月3000円切るくらい
 全てが動的アクセスではない


バージョニング
==============================

- ブルーグリーンデプロイ
- カナリアリリース

.. rst-class:: presenter-notes

 事前に別バージョンを準備してバージョンを変えてみる


StackDriver
==============================

- Logging
- Monitoring
- Alert
- Debugger


SSLにも対応
==============================

- デフォルトでSSLに対応
- 独自ドメインにも対応
- 無料

.. rst-class:: presenter-notes

 secure:alwaysのベージを開く
 .ioのドメインを紐づけておく
 設定画面を見せる


静的サイトのホスティング
==============================

- 転送量のみでスタティックサーバから配信できる
- Googleの強力なキャッシュサーバにのる

  - キャッシュにのれば無料

`静的サイトホスティングの為のGCS/GAE/Firebase Hosting比較 <https://medium.com/google-cloud-jp/%E9%9D%99%E7%9A%84%E3%82%B5%E3%82%A4%E3%83%88%E3%83%9B%E3%82%B9%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%AE%E7%82%BA%E3%81%AEgcs-gae-firebase-hosting%E6%AF%94%E8%BC%83-e7d406609f2e>`_  

.. rst-class:: presenter-notes

 ブログをGAEでホスティングしているのを紹介


便利機能
==============================

- タスクキュー
- cron
- Memcache (First Gen)
- アクセス制御 

  - Googleアカウント、G Suite


デモ
==============================


まとめ
==============================

App Engineを使うことで

- 運用いらずでアプリを作るのに集中できる
- 大量アクセスでもぐっすり眠れる
- 個人的にGoogleのインフラで動いているという安心感


まだ触ったことがない人は一度使ってみてはいかがでしょうか。


ありがとうございました
==============================



