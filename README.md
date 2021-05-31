# jismesh

地域メッシュコード [JISX0410:2002](https://www.jisc.go.jp/app/jis/general/GnrJISNumberNameSearchList?show&jisStdNo=X0410) に関するユーティリティです。

## 対応地域メッシュコード
- 1次(標準地域メッシュ 80km四方): 1
- 40倍(拡張統合地域メッシュ 40km四方): 40000
- 20倍(拡張統合地域メッシュ 20km四方): 20000
- 16倍(拡張統合地域メッシュ 16km四方): 16000
- 2次(標準地域メッシュ 10km四方): 2
- 8倍(拡張統合地域メッシュ 8km四方): 8000
- 5倍(統合地域メッシュ 5km四方): 5000
- 4倍(拡張統合地域メッシュ 4km四方): 4000
- 2.5倍(拡張統合地域メッシュ 2.5km四方): 2500
- 2倍(統合地域メッシュ 2km四方): 2000
- 3次(標準地域メッシュ 1km四方): 3
- 4次(分割地域メッシュ 500m四方): 4
- 5次(分割地域メッシュ 250m四方): 5
- 6次(分割地域メッシュ 125m四方): 6
- 7次(62.5m四方)*: 7
- 8次(31.25m四方)*: 8
- 9次(15.625m四方)*: 9
- 10次(7.8125m四方)*: 10


\* 7次以降は [JISX0410:2002](https://www.jisc.go.jp/app/jis/general/GnrJISNumberNameSearchList?show&jisStdNo=X0410) の規定外ですが、実務上のニーズに応えるため本ユーティリティでは取り扱い可能としています。
それらの次数を使用した場合は、`JismeshNonstandardWarning`の警告が表示されます。

  
## インストール
```bash
pip install jismesh
```

## 緯度経度から地域メッシュコードを求める

メッシュコードに変換する世界測地系緯度経度と変換するメッシュコードの次数を指定します。

### 使用例
```python
import jismesh.utils as ju

# 緯度経度からメッシュコードを求める。
meshcode = ju.to_meshcode(35.658581, 139.745433, 3)
print(meshcode)
53393599

# pandas DataFrame中の緯度経度をメッシュコードに変換する。
import pandas as pd
df = pd.DataFrame({'lat': [35.658581, 34.987574], 'lon':[139.745433, 135.759363]})
print(df)
         lat         lon
0  35.658581  139.745433
1  34.987574  135.759363

df['meshcode'] = ju.to_meshcode(df.lat, df.lon, 3)
print(df)
         lat         lon  meshcode
0  35.658581  139.745433  53393599
1  34.987574  135.759363  52353680
```


## 地域メッシュコードから次数を求める

メッシュコードからそのメッシュコードの次数を判定します。

### 使用例
```python
import jismesh.utils as ju

# メッシュコードの次数を求める。
meshlevel = ju.to_meshlevel(53393599)
print(meshlevel)
3

# pandas DataFrame中のメッシュコードを次数に変換する。
import pandas as pd
df = pd.DataFrame({'meshcode': [53393599, 52353680]})
print(df)
   meshcode
0  53393599
1  52353680

df['level'] = ju.to_meshlevel(df.meshcode)
print(df)
   meshcode  level
0  53393599      3
1  52353680      3
```
 

## 地域メッシュコードから緯度経度を求める

求める緯度経度で表される点は、当該メッシュの基準点(南西端)から、
緯度座標上の点の位置(当該メッシュの単位経度の倍数)、経度座標上の点の位置(当該メッシュの単位緯度の倍数)
を指定します。

### 使用例
```python
import jismesh.utils as ju
    
# 南西端の緯度経度を求める。
lat_sw, lon_sw = ju.to_meshpoint(53393599, 0, 0)
print(lat_sw, lon_sw)
35.6583333333 139.7375
    
# 北東端の緯度経度を求める。
lat_ne, lon_ne = ju.to_meshpoint(53393599, 1, 1)
print(lat_ne, lon_ne)
35.6666666667 139.75
    
# 中心点の緯度経度を求める。
lat_c, lon_c = ju.to_meshpoint(53393599, 0.5, 0.5)
print(lat_c, lon_c)
35.6625 139.74375

# 東隣接メッシュの中心点の緯度経度を求める。
lat_east_neighbor_c, lon_east_neighbor_c = ju.to_meshpoint(53393599, 0.5, 1.5)
print(lat_east_neighbor_c, lon_east_neighbor_c)
35.6625 139.75625

# pandas DataFrame中のメッシュコードを中心点緯度経度に変換する。
import pandas as pd
df = pd.DataFrame({'meshcode': [53393599, 52353680]})
print(df)
   meshcode
0  53393599
1  52353680

df['lat'], df['lon'] = ju.to_meshpoint(df.meshcode, lat_multiplier=0.5, lon_multiplier=0.5) 
print(df)
   meshcode      lat        lon
0  53393599  35.6625  139.74375
1  52353680  34.9875  135.75625
```

## 交差する地域メッシュコードを求める

### 使用例
```python
import jismesh.utils as ju
    
# 交差するメッシュコードを求める。
generator_intersects = ju.to_intersects(53394611, 4)

for meshcode in generator_intersects:
	print(meshcode)
    
533946111
533946112
533946113
533946114
```

