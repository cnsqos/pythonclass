import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np
from math import pi

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 공통 함수: TOP10 범례
def draw_top10_legend(ax, top10_df, colors, title):
    patches = []
    for i, (player, color) in enumerate(zip(top10_df['Player'], colors), start=1):
        patches.append(
            mpatches.Patch(color=color, label=f"{i}. {player}")
        )

    ax.legend(
        handles=patches,
        title=title,
        bbox_to_anchor=(1.02, 1),
        loc='upper left',
        frameon=True
    )


df = pd.read_csv("data/players_data-2024_2025.csv")

#전처리
df['MainPos'] = df['Pos'].str.split(',').str[0]
df_played = df[df['Min'] >= 900]
df_def = df_played[df_played['MainPos'] == 'DF']


# 1. 나이 분포
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
sns.histplot(df['Age'], bins=15, kde=True, color='coral', ax=ax)
ax.set_title("선수 나이 분포")
plt.show()


# 2. 포지션별 선수 수
fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)
sns.countplot(data=df, x='MainPos', color='coral', ax=ax)
ax.set_title("포지션별 선수 분포")
plt.show()


# 3. 득점력 분석 (xG vs Gls)
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

sns.regplot(
    data=df_played,
    x='xG',
    y='Gls',
    scatter_kws={'alpha':0.25, 'color':'coral'},
    line_kws={'color':'coral'},
    ax=ax
)

top_scorers = df_played.nlargest(10, 'Gls').reset_index(drop=True)
colors = sns.color_palette("tab10", 10)

for i, row in top_scorers.iterrows():
    ax.scatter(row['xG'], row['Gls'], color=colors[i], s=80, edgecolor='black', zorder=3)

draw_top10_legend(ax, top_scorers, colors, "득점 TOP 10")
ax.set_title("기대득점(xG) vs 실제득점")
plt.show()


# 4. 포지션별 득점 분포
fig, ax = plt.subplots(figsize=(6, 5), constrained_layout=True)
sns.boxplot(data=df_played, x='MainPos', y='Gls', color='coral', ax=ax)
ax.set_title("포지션별 득점 분포")
plt.show()


# 5. 클럽별 수비 기여도
fig, ax = plt.subplots(figsize=(18, 8), constrained_layout=True)
sns.barplot(data=df_def, x='Squad', y='Tkl+Int', color='coral', ax=ax)
ax.set_title("클럽별 수비 기여도")
ax.tick_params(axis='x', rotation=90)
plt.show()


# 6. 패스 & 창의성 (PrgP vs KP)
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

sns.regplot(
    data=df_played,
    x='PrgP',
    y='KP',
    scatter_kws={'alpha':0.25, 'color':'coral'},
    line_kws={'color':'coral'},
    ax=ax
)

top_playmakers = df_played.nlargest(10, 'KP').reset_index(drop=True)
colors = sns.color_palette("tab10", 10)

for i, row in top_playmakers.iterrows():
    ax.scatter(row['PrgP'], row['KP'], color=colors[i], s=80, edgecolor='black', zorder=3)

draw_top10_legend(ax, top_playmakers, colors, "창의성 TOP 10")
ax.set_title("전진 패스 vs 키 패스")
plt.show()


# 7. 볼 소유 리스크 (Carries vs Dis)
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

sns.regplot(
    data=df_played,
    x='Carries',
    y='Dis',
    scatter_kws={'alpha':0.25, 'color':'coral'},
    line_kws={'color':'coral'},
    ax=ax
)

top_dribblers = df_played.nlargest(10, 'Carries').reset_index(drop=True)
colors = sns.color_palette("tab10", 10)

for i, row in top_dribblers.iterrows():
    ax.scatter(row['Carries'], row['Dis'], color=colors[i], s=80, edgecolor='black', zorder=3)

draw_top10_legend(ax, top_dribblers, colors, "볼 운반 TOP 10")
ax.set_title("볼 운반 vs 소유권 상실")
plt.show()


# 8. 어시스트 분석 (xA vs Ast)
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

sns.regplot(
    data=df_played,
    x='xA',
    y='Ast',
    scatter_kws={'alpha':0.25, 'color':'coral'},
    line_kws={'color':'coral'},
    ax=ax
)

top_assisters = df_played.nlargest(10, 'Ast').reset_index(drop=True)
colors = sns.color_palette("tab10", 10)

for i, row in top_assisters.iterrows():
    ax.scatter(row['xA'], row['Ast'], color=colors[i], s=80, edgecolor='black', zorder=3)

draw_top10_legend(ax, top_assisters, colors, "어시스트 TOP 10")
ax.set_title("기대 어시스트(xA) vs 실제 어시스트")
plt.show()


# 9. 패스 정확도 (Cmp% vs PrgP)
fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

sns.scatterplot(
    data=df_played,
    x='Cmp%',
    y='PrgP',
    color='coral',
    alpha=0.25,
    ax=ax
)

top_pass_acc = df_played.nlargest(10, 'Cmp%').reset_index(drop=True)
colors = sns.color_palette("tab10", 10)

for i, row in top_pass_acc.iterrows():
    ax.scatter(row['Cmp%'], row['PrgP'], color=colors[i], s=80, edgecolor='black', zorder=3)

draw_top10_legend(ax, top_pass_acc, colors, "패스 정확도 TOP 10")
ax.set_title("패스 성공률 vs 전진 패스")
ax.set_xlabel("패스 성공률 (%)")
ax.set_ylabel("전진 패스 수")
plt.show()


# 10. 주요 지표 상관관계
cols = ['Gls', 'Ast', 'xG', 'xA', 'PrgP', 'KP', 'Tkl', 'Int']
corr = df_played[cols].corr()

fig, ax = plt.subplots(figsize=(7, 6), constrained_layout=True)
sns.heatmap(corr, annot=True, cmap='Reds', ax=ax)
ax.set_title("주요 지표 상관관계")
plt.show()



# 11. 포지션별 득점 TOP10
positions = ['FW', 'MF', 'DF']

for pos in positions:
    df_pos = df_played[df_played['MainPos'] == pos]

    if len(df_pos) < 10:
        continue

    fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)

    sns.regplot(
        data=df_pos,
        x='xG',
        y='Gls',
        scatter_kws={'alpha':0.25, 'color':'coral'},
        line_kws={'color':'coral'},
        ax=ax
    )

    top10 = df_pos.nlargest(10, 'Gls').reset_index(drop=True)
    colors = sns.color_palette("tab10", 10)

    for i, row in top10.iterrows():
        ax.scatter(
            row['xG'],
            row['Gls'],
            color=colors[i],
            s=80,
            edgecolor='black',
            zorder=3
        )

    draw_top10_legend(ax, top10, colors, f"{pos} 득점 TOP 10")

    ax.set_title(f"{pos} 포지션 득점력 비교 (xG vs Gls)")
    ax.set_xlabel("기대득점 (xG)")
    ax.set_ylabel("득점 (Gls)")
    plt.show()




# 12. 레알 마드리드 vs 바르셀로나 팀 비교

teams = ['Real Madrid', 'Barcelona']
df_team = df_played[df_played['Squad'].isin(teams)]

# 비교 지표 확장
metrics = [
    'Gls', 'xG', 'Ast', 'xA',
    'KP', 'PrgP', 'PrgC',
    'Carries', 'Dis',
    'Tkl', 'Int', 'Tkl+Int'
]

team_stats = (
    df_team
    .groupby('Squad')[metrics]
    .mean()
)

# -------------------------
# 서브플롯 생성
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(18, 6), constrained_layout=True)

# Real Madrid
team_stats.loc['Real Madrid'].plot(
    kind='bar',
    ax=axes[0],
    color='steelblue'
)
axes[0].set_title("Real Madrid 평균 지표", fontsize=12)
axes[0].set_ylabel("경기당 평균")
axes[0].set_xlabel("지표")
axes[0].tick_params(axis='x', rotation=45)

# Barcelona
team_stats.loc['Barcelona'].plot(
    kind='bar',
    ax=axes[1],
    color='indianred'
)
axes[1].set_title("Barcelona 평균 지표", fontsize=12)
axes[1].set_ylabel("경기당 평균")
axes[1].set_xlabel("지표")
axes[1].tick_params(axis='x', rotation=45)

plt.show()




plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

teams = ['Real Madrid', 'Barcelona']
df_team = df_played[df_played['Squad'].isin(teams)]

metrics = [
    'Gls', 'xG', 'Ast', 'xA',
    'KP', 'PrgP',
    'Tkl+Int'
]

team_stats = (
    df_team
    .groupby('Squad')[metrics]
    .mean()
    .loc[teams]
)

# ======================================================
# Difference Bar (Real Madrid - Barcelona)
# ======================================================
diff = team_stats.loc['Real Madrid'] - team_stats.loc['Barcelona']
pct_diff = (diff / team_stats.loc['Barcelona']) * 100

x = np.arange(len(metrics))
colors = ['steelblue' if v > 0 else 'indianred' for v in diff]

fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)

bars = ax.bar(x, diff, color=colors)

for i, bar in enumerate(bars):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{diff[i]:.2f}\n({pct_diff[i]:+.1f}%)",
        ha='center',
        va='bottom' if diff[i] > 0 else 'top',
        fontsize=9
    )

ax.axhline(0, color='black', linewidth=1)
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45)
ax.set_title("Difference Bar (Real Madrid - Barcelona)")
ax.set_ylabel("경기당 평균 차이")

plt.show()

# ======================================================
# 핵심 지표 하이라이트 비교
# ======================================================
highlight_metrics = ['Gls', 'xG', 'KP', 'PrgP', 'Tkl+Int']
highlight_stats = team_stats[highlight_metrics]

x = np.arange(len(highlight_metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

bars_rm = ax.bar(
    x - width / 2,
    highlight_stats.loc['Real Madrid'],
    width,
    label='Real Madrid',
    color='steelblue'
)

bars_bar = ax.bar(
    x + width / 2,
    highlight_stats.loc['Barcelona'],
    width,
    label='Barcelona',
    color='indianred'
)

for bars in [bars_rm, bars_bar]:
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{bar.get_height():.2f}",
            ha='center',
            va='bottom',
            fontsize=9
        )

ax.set_title("핵심 지표 하이라이트 비교")
ax.set_xticks(x)
ax.set_xticklabels(highlight_metrics)
ax.set_ylabel("경기당 평균")
ax.legend()

plt.show()

# ======================================================
# Radar Chart 요약 (정규화)
# ======================================================
radar_metrics = [
    'Gls', 'xG', 'Ast', 'xA',
    'KP', 'PrgP',
    'Tkl+Int'
]

radar_stats = team_stats[radar_metrics]

# 정규화 (0~1)
radar_norm = radar_stats / radar_stats.max()

labels = radar_metrics
num_vars = len(labels)

angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Real Madrid
values_rm = radar_norm.loc['Real Madrid'].tolist()
values_rm += values_rm[:1]

ax.plot(angles, values_rm, color='steelblue', linewidth=2, label='Real Madrid')
ax.fill(angles, values_rm, color='steelblue', alpha=0.25)

# Barcelona
values_bar = radar_norm.loc['Barcelona'].tolist()
values_bar += values_bar[:1]

ax.plot(angles, values_bar, color='indianred', linewidth=2, label='Barcelona')
ax.fill(angles, values_bar, color='indianred', alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])
ax.set_title("Radar Chart 요약: Real Madrid vs Barcelona", fontsize=13)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.show()