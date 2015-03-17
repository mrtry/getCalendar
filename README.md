# getCalendar

---

## Overview

gdataを使って、指定したカレンダーから情報を抜き出す

## Description

指定したカレンダーから当日、前日の登録されたタスク名を抜き出しprintする。
infinite loopさんの[ゆっくりが今日の予定を教えてくれる](http://www.infiniteloop.co.jp/blog/2014/03/yukkuri-hisho/)がPHPで作っていたものを、pythonで似たものを作成したもの。
指定時刻に実行し、テキストを作成し、音声合成で読ませようと考えていたが熱が冷めてそのままに。

## Requirement

[gdata](https://developers.google.com/google-apps/calendar/)が必要

## Usage

scriptにUIDとPW、対象とするCalendarIDを入力し実行する。
![usage](https://dl.dropboxusercontent.com/u/33568010/github/Screenshot%20from%202014-06-13%2010%3A18%3A37.png)
