import matplotlib.pyplot as plt
import numpy as np
import re

def generate_general_stacked_bar_graph(df, variable_map, tgt_var):
    fig, ax = plt.subplots(figsize=(10, 4))
    categories = df[tgt_var].unique()
    drop_counts = []
    graduate_counts = []
    for degree in categories:
        count_entries = df[df[tgt_var] == degree]['dropout'].value_counts()
        if "Dropout" in count_entries:
            drop_counts.append(count_entries["Dropout"])
        else:
            drop_counts.append(0)
        if "Graduate" in count_entries:
            graduate_counts.append(count_entries["Graduate"])
        else:
            graduate_counts.append(0)

    # categories = [variable_map[tgt_var][course] for course in variable_map[tgt_var]]
    categories = [variable_map[tgt_var][c] for c in categories]
    categories = [c.replace(";", '') for c in categories]
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=70, ha='right', fontsize=12)
    plt.bar(categories, drop_counts, color='r', label="dropout")
    plt.bar(categories, graduate_counts, bottom=drop_counts, color='b', label="graduate")

    ax.set_ylabel('Students', fontsize=16)
    ax.set_xlabel(tgt_var, fontsize=16)
    ax.set_title(f'Graduation vs Dropout Rates of Students by {tgt_var}', fontsize=16)
    ax.legend()
    plt.show()

def generate_stacked_bar_graph(df, variable_map):
    fig, ax = plt.subplots(figsize=(10, 8))
    categories = df['Course'].unique()
    drop_counts = []
    graduate_counts = []
    for degree in categories:
        count_entries = df[df['Course'] == degree]['dropout'].value_counts()
        drop_counts.append(count_entries["Dropout"])
        graduate_counts.append(count_entries["Graduate"])

    categories = [variable_map["Course"][course] for course in variable_map["Course"]]
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=90, ha='right')
    plt.bar(categories, drop_counts, color='r', label="dropout")
    plt.bar(categories, graduate_counts, bottom=drop_counts, color='b', label="graduate")

    ax.set_ylabel('Students')
    ax.set_title('Graduation vs Dropout Rates of Students')
    ax.legend()
    plt.show()

def jitter_plot(df):
    plt.figure(figsize=(10, 4))
    PREV_QUAL = 'Previous qualification (grade)'
    ADMISSION_GRADE = 'Admission grade'
    # adding jitter to elements to prevent repeats:
    dropout_prev_qual = df[PREV_QUAL][df['dropout'] == 'Dropout'].to_numpy()
    dropout_prev_score = df[ADMISSION_GRADE][df['dropout'] == 'Dropout'].to_numpy()
    jitter = 0.25 * np.random.randn(dropout_prev_score.shape[0])
    dropout_prev_qual += jitter
    dropout_prev_score += jitter

    dropout_midway = int(dropout_prev_qual.shape[0] / 2)
    plt.scatter(dropout_prev_qual[:dropout_midway], dropout_prev_score[:dropout_midway], color='red', label='Dropout',s=4)

    graduate_prev_qual = df[PREV_QUAL][df['dropout'] == 'Graduate']
    graduate_prev_score = df[ADMISSION_GRADE][df['dropout'] == 'Graduate']
    jitter = 0.25 * np.random.randn(graduate_prev_score.shape[0])
    graduate_prev_score += jitter
    graduate_prev_qual += jitter

    graduate_midway = int(3 * graduate_prev_qual.shape[0] / 4)
    plt.scatter(graduate_prev_qual[:graduate_midway], graduate_prev_score[:graduate_midway], color='blue', label='Graduate',s=4)
    plt.scatter(dropout_prev_qual[dropout_midway:], dropout_prev_score[dropout_midway:], color='red',s=4)
    plt.scatter(graduate_prev_qual[graduate_midway:], graduate_prev_score[graduate_midway:], color='blue',s=4)

    plt.xlabel('Past Grades', fontsize=16)
    plt.ylabel('Admission Score', fontsize=16)
    plt.legend(fontsize=16)
    plt.title('Comparison between Admission Scores and Grades vs Dropout',fontsize=16)
    plt.grid(True)
    plt.show()

def pie_chart(y_col):
    unique, counts = np.unique(y_col, return_counts=True)
    plt.figure(figsize=(4, 4))
    plt.pie(counts, labels=unique, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, (p / 100) * sum(counts)), colors = ['red', 'blue', 'green'])
    plt.title('Dropout Proportion/Counts',fontsize=16)
    plt.axis('equal')
    plt.show()

def plot_semester_compare_bp(df, curriculum_units):

    plot_df = df[list(curriculum_units)]
    clean_text = lambda x: re.sub(r'(Curricular units |\(|\))', '', x)
    desired_order = [clean_text(x) for x in curriculum_units]
    pairs = [(desired_order[i], desired_order[i + 1]) for i in range(0, len(desired_order), 2)]
    plot_df = plot_df.rename(columns={x: clean_text(x) for x in curriculum_units})
    # plot_df.boxplot(vert=False)

    fig, axes = plt.subplots(len(pairs), 1, figsize=(8, 12))
    fig.subplots_adjust(hspace=0.5)

    for i, ax in enumerate(axes):
        renamed_df = plot_df.copy().rename(columns={x: " ".join(x.split()[:2]) for x in pairs[i]})
        renamed_df[['1st sem', '2nd sem']].boxplot(vert=False, ax=ax)
        title = " ".join(pairs[i][0].split()[2:])
        ax.set_title(f"{title} Curricular units between 1st and 2nd sem")
        # ax.set_yticklabels("units", rotation=45, ha='right')
        for j, column in enumerate(['1st sem', '2nd sem']):
            q1 = renamed_df[column].quantile(0.25)
            median = renamed_df[column].median()
            q3 = renamed_df[column].quantile(0.75)

            y_pos = j + 1
            all_summary = f'Q1: {q1:.2f} | Median: {median:.2f} | Q3: {q3:.2f}'
            ax.text(median - 0.5, y_pos + 0.4, all_summary, verticalalignment='top', color='red', fontsize=9)

    fig.suptitle("Curricular Units between 1st and 2nd Semester", fontsize=16)

    plt.show()

def plot_grad_drop_compare_bp(df, curriculum_units, sem):
    if '1' in sem:
        filtered_units = [x for x in curriculum_units if '1' in x]
    else:
        filtered_units = [x for x in curriculum_units if '2' in x]
    plot_df = df[list(filtered_units) + ['dropout']]
    if '1' in sem:
        clean_text = lambda x: re.sub(r'(Curricular units 1st sem |\(|\))', '', x)
    else:
        clean_text = lambda x: re.sub(r'(Curricular units 2nd sem |\(|\))', '', x)

    plot_df = plot_df.rename(columns={x: clean_text(x) for x in filtered_units})
    units = [clean_text(x) for x in filtered_units]
    # plot_df.boxplot(vert=False)

    fig, axes = plt.subplots(len(filtered_units), 1, figsize=(8, 5))
    fig.subplots_adjust(hspace=0.5)

    for i, ax in enumerate(axes):
        dropout = plot_df[plot_df['dropout'] == "Dropout"][units[i]].to_numpy()
        graduate = plot_df[plot_df['dropout'] == "Graduate"][units[i]].to_numpy()

        # ax.boxplot([dropout, graduate], labels=["Dropout", "Graduate"], vert=False)
        ax.boxplot([dropout, graduate], labels=["Dropout", "Graduate"], vert=False)

        if '1' in sem:
            title = f'Curricular units 1st sem ({units[i]})'
        else:
            title = f'Curricular units 2nd sem ({units[i]})'
        ax.set_title(f"{title}")
        dropout_q1 = np.percentile(dropout, 25)
        dropout_median = np.median(dropout)
        dropout_q3 = np.percentile(dropout, 75)

        graduate_q1 = np.percentile(graduate, 25)
        graduate_median = np.median(graduate)
        graduate_q3 = np.percentile(graduate, 75)

        graduate_summary = f'Q1: {graduate_q1:.2f} | Median: {graduate_median:.2f} | Q3: {graduate_q3:.2f}'
        dropout_summary = f'Q1: {dropout_q1:.2f} | Median: {dropout_median:.2f} | Q3: {dropout_q3:.2f}'
        # ax.text(dropout_median - 1.25, 1 + 0.4, dropout_summary, verticalalignment='top', color='red', fontsize=9)
        ax.text((graduate_q1 + graduate_q3)/2 - 2, 1 + 0.4, dropout_summary, verticalalignment='top', color='red', fontsize=9)
        # ax.text(graduate_median - 1.25, 2 + 0.4, graduate_summary, verticalalignment='top', color='red', fontsize=9)
        ax.text((graduate_q1 + graduate_q3)/2 - 2, 2 + 0.4, graduate_summary, verticalalignment='top', color='red', fontsize=9)

    # Set a common title for the whole figure
    if '1' in sem:
        fig.suptitle("1st Semester Curricular Units by Dropout", fontsize=16)
    else:
        fig.suptitle("2nd Semester Curricular Units by Dropout", fontsize=16)

    # Display the plots
    plt.show()


def plot_line_graph(df, tgt_col):
    tgt_df = df[[tgt_col, 'dropout']]
    unique_inflation = tgt_df[tgt_col].unique()
    inf_counts = {}
    for inf in sorted(unique_inflation):
        filtered_df = tgt_df[tgt_df[tgt_col] == inf]
        dropout_count = filtered_df[filtered_df['dropout'] == 'Dropout'].shape[0]
        graduate_count = filtered_df[filtered_df['dropout'] == 'Graduate'].shape[0]
        inf_counts[inf] = {'dropout_count': dropout_count, 'graduate_count': graduate_count}

    inf_rate = list(inf_counts.keys())
    dropout_count = [inf_counts[key]['dropout_count'] for key in inf_counts.keys()]
    graduate_count = [inf_counts[key]['graduate_count'] for key in inf_counts.keys()]
    combined_count = [dropout_count[i] + graduate_count[i] for i in range(len(dropout_count))]
    plt.figure(figsize=(8, 3))
    plt.plot(inf_rate, dropout_count, marker='o', color='red', linestyle='-', linewidth=2, markersize=6,
             label="Dropout Students")
    plt.plot(inf_rate, graduate_count, marker='o', color='green', linestyle='-', linewidth=2, markersize=6,
             label="Graduated Students")
    plt.plot(inf_rate, combined_count, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6,
             label='Total Students')
    plt.legend()
    plt.title(f"Student Performance vs {tgt_col}")
    plt.ylabel("Count of Students")
    custom_xticks = list(set(inf_rate) - {0.5, 1.79, 1.74, 12.7, 11.1})
    print(custom_xticks)
    plt.xticks(custom_xticks)
    plt.grid()
    plt.xlabel("Inflation Rate")
    plt.show()
