import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config.ga_config import (POPULATION_SIZE, LOWER_BOUND, UPPER_BOUND,
                              GENERATION_COUNT, MUTATION_RATE,CROSS_OVER_RATE_RATE)
from core.algorithm import genetic_algorithm
import altair as alt


st.set_page_config(layout="wide")

if "population_size" not in st.session_state:
    st.session_state["population_size"] = POPULATION_SIZE
    st.session_state["lower_bound"] = LOWER_BOUND
    st.session_state["upper_bound"] = UPPER_BOUND
    st.session_state["generations"] = GENERATION_COUNT
    st.session_state["mutation_rate"] = MUTATION_RATE
    st.session_state["crossover_rate"] = CROSS_OVER_RATE_RATE

col1, col2, col3 = st.columns(3)

with col1:
    population_size = st.number_input("population_size", min_value=20, max_value=500, placeholder=f"ex : {POPULATION_SIZE}",
                                      key="population_size")
    generations = st.number_input("generations", min_value=5, max_value=50, placeholder=f"ex : {GENERATION_COUNT}", key="generations")

with col2:
    upper_bound = st.number_input("upper_bound", min_value=0, placeholder=f"ex : {UPPER_BOUND}", key="upper_bound")
    lower_bound = st.number_input("lower_bound", max_value=0, placeholder=f"ex : {LOWER_BOUND}", key="lower_bound")

with col3:
    crossover_rate = st.number_input("crossover_rate", min_value=0.0, max_value=1.0, placeholder=f"ex : {CROSS_OVER_RATE_RATE}",
                                     key="crossover_rate")
    mutation_rate = st.number_input("mutation_rate", min_value=0.0, max_value=1.0, step=.01, placeholder=f"ex : {MUTATION_RATE}",
                                    key="mutation_rate")


if st.session_state["population_size"] is None\
        or st.session_state["lower_bound"] is None\
        or st.session_state["upper_bound"] is None\
        or st.session_state["generations"] is None\
        or st.session_state["mutation_rate"] is None\
        or st.session_state["crossover_rate"] is None:
    st.error("You must fully complete add all variables.")
else:
    _, button_col, _ = st.columns([2, 4, 2])
    if button_col.button("start", width="stretch"):
        st.badge("Success", icon=":material/check:", color="green")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.subheader("population size", text_alignment="center")
            st.subheader(f":blue[{st.session_state["population_size"]}]", text_alignment="center")
        with col2:
            st.subheader("generations", text_alignment="center")
            st.subheader(f":blue[{st.session_state["generations"]}]", text_alignment="center")
        with col3:
            st.subheader("lower bound", text_alignment="center")
            st.subheader(f":blue[{st.session_state["lower_bound"]}]", text_alignment="center")
        with col4:
            st.subheader("upper bound", text_alignment="center")
            st.subheader(f":blue[{st.session_state["upper_bound"]}]", text_alignment="center")
        with col5:
            st.subheader("crossover rate", text_alignment="center")
            st.subheader(f":blue[{st.session_state["crossover_rate"]}]", text_alignment="center")
        with col6:
            st.subheader("mutation rate", text_alignment="center")
            st.subheader(f":blue[{st.session_state["mutation_rate"]}]", text_alignment="center")

        A_B_C_generations, fitness_generations = genetic_algorithm(
            st.session_state["population_size"], st.session_state["generations"],
            st.session_state["lower_bound"], st.session_state["upper_bound"],
            st.session_state["mutation_rate"], st.session_state["crossover_rate"]
        )

        col1_graph, col2_graph = st.columns(2)

        # ---------------------------
        # graph fitness & generations
        with col1_graph:
            st.caption(f"fitness & generations graph", sttext_alignment="center")
            st.line_chart(fitness_generations)  # graph fitness & generations

        a, b, c = [], [], []
        best_a_fitness_generations, best_b_fitness_generations, best_c_fitness_generations = [], [], []

        for generation in A_B_C_generations:
            a, b, c = map(list, zip(*generation))
            best_a_fitness_generations.append(min(a))
            best_b_fitness_generations.append(min(b))
            best_c_fitness_generations.append((min(c)))
        col1, col2, col3 = st.columns(3)
        scatter_charts = (
            ("a", a, col1),
            ("b", b, col2),
            ("c", c, col3)
        )

        # ---------------------------------------------------
        # Final Generation Population Solutions scatter chart
        for chart_inf in scatter_charts:
            df = pd.DataFrame({'y': chart_inf[1]})
            df['x'] = range(len(chart_inf[1]))
            closest_val = min(chart_inf[1], key=abs)
            df['is_closest'] = abs(df['y']) == abs(closest_val)
            chart = alt.Chart(df).mark_circle(size=60).encode(
                x=alt.X('x', title=f'individuals for last generation {st.session_state["generations"]}'),
                y=alt.Y('y', title=f'values of {chart_inf[0]}'),
                color=alt.condition(
                    alt.datum.is_closest == True,
                    alt.value('red'),
                    alt.value('blue')
                ),
                tooltip=['x', 'y']  # Optional tooltip
            ).interactive()
            chart_inf[2].caption(f"Final Generation {st.session_state["generations"]} Population Solutions for ({chart_inf[0]})",
                                   text_alignment="center")
            chart_inf[2].altair_chart(chart, use_container_width=True)  # Final Generation Population Solutions scatter chart

        # ---------------------------------
        # Parameter Values Over Generations
        with col2_graph:
            fitness_generations = pd.DataFrame({
                'a': best_a_fitness_generations,
                'b': best_b_fitness_generations,
                'c': best_c_fitness_generations
            })
            st.caption("Parameter Values Over Generations", text_alignment="center")
            st.line_chart(fitness_generations)  # Parameter Values Over Generations

        # --------------------------------------
        # Quadratic Function For All Generations
        x_values = np.linspace(-10, 10, num=50)
        fig, ax = plt.subplots(figsize=(10, 6))
        for i in range(st.session_state["generations"]):
            a = best_a_fitness_generations[i]
            b = best_b_fitness_generations[i]
            c = best_c_fitness_generations[i]
            y = a * (x_values ** 2) + b * x_values + c
            ax.plot(x_values, y, label=f'Curve {i + 1} (a={a}, b={b}, c={c})')
        ax.set_xlabel('X Values')
        ax.set_ylabel('Y Values')
        ax.set_title('Quadratic Curves')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True)
        st.caption("Quadratic Function For All Generations", text_alignment="center")
        st.pyplot(fig)  # Quadratic Function For All Generations
