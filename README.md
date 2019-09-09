
# PyACO

PyACOはPython向けの       
ACO(Ant Colony Optimization)     
アントコロニー最適化の実装です。

ACOの概要・使用方法は後ほどQiitaにまとめます。

# インストール

```
pip install PyACO
```

# 基本使用方法

main.py
```python
from PyACO.ACOSolver import ACOSolver

# Solverインスタンス
aco_solver = ACOSolver(num_of_ants=30, num_of_vertexes=50, Q=100, alpha=3, beta=5, rou=0.9, max_iterations=300,
                       initial_vertex=0, tau_min=0, tau_max=3000, ant_prob_random=0.1, super_not_change=30, plot_time=0.2)

# 実行
aco_solver.run_aco()
```

- num_of_ants
    - 蟻の数
- num_of_vertexes
    - グラフの頂点数
    - 辺は現状各頂点間に張られます
- Q
    - Qiita参照
- alpha
    - Qiita参照
- beta
    - Qiita参照
- rou
    - Qiita参照
- max_iterations
    - ACOのサイクル回数
- initial_vertex
    - どの頂点から出発するか
- tau_min   
    - 各辺のフェロモンの最小許容ライン
    - tau_minが0.1なら、0.1以上になるように丸められます
- tau_max
    - 各辺のフェロモンの最大許容ライン
    - tau_minが3.0なら、3.0以下になるように丸められます
- ant_prob_random
    - ant_prob_randomによって、蟻がランダムに道選択するかが決まります
    - [0, 1]の間の小数を指定してください。
    - 大きい値を指定すればするほど、ランダムに動きます
- super_not_change
    - スーパーベストスコアがこのsuper_not_change回数だけ変化しないとき、フェロモンを強制的にリセットします。
    - フェロモンが溜まって停滞することがあるため、それの強制回避策です。
- plot_time
    - matplotlibの更新回数です。
    


# ファイル構成

## PyACO/ACOSolver.py

ACOSolver.pyは、ACOを実行するための
全体管理のクラスです。

## PyACO/Graph.py

ACOでは、組み合わせ最適化問題をグラフ構造に帰結します。
Graph.pyはそのグラフ構造の実装クラス・ファイルです。

## PyACO/Colony.py

num_of_ants匹の蟻が住むコロニーを模したクラス・ファイルです。
これら蟻に指示を出す、管理をするクラスになっています。

## PyACO/Ant.py

各蟻のクラスです。

- フェロモンによる移動選択
- 移動した経路によるフェロモン構築

などを行います。

## PyACO/Parameters.py

ACOで使用するパラメータを保持する
クラスです。

## PyACO/plot.py

Matplotlibを利用して現状のグラフの状態を可視化します。


# 注意点

正しいPythonの使用方法がわかっていないため
これらのPyACO以下のファイルは互いに参照をしています。

- ACOSolver
    - Parameters
    - Colony
    - Graph
    - plot
- Graph
    - Parameters
- Colony
    - Parameters
    - Graph
    - Ant
- Ant
    - Parameters
    - Graph

上記の表し方は、例えば
GraphはParametersを参照しています。


# 改修点

- グラフのランダム構成
    - 現在は各頂点に各頂点が繋がっている
- NetworkXなどのグラフライブラリからのネットワーク読み込み対応
- ASrank, ASeliteなどの有名ACOの対応実装
- ファイル構成
    - 正しいのか分からない


# ライセンス

MIT









