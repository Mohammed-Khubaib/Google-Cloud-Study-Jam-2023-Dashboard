import streamlit as st
import time
import math
st.cache(allow_output_mutation=True)
def progressBar(tier_name, tier_limit, Tyes_count, color, emoji, target_emoji):
    if Tyes_count <= tier_limit:
        st.markdown(f"#### {tier_name} {emoji}:  :{color}[{Tyes_count}/{tier_limit} participants] {target_emoji}")
        tier = st.progress(0)
        for percent_complete in range(Tyes_count + 1):
            time.sleep(0.01)
            tier.progress(percent_complete / tier_limit, f"Total completion {math.trunc((percent_complete / tier_limit) * 100)} %")
    else:
        st.markdown(f"#### {tier_name} {emoji}:  :{color}[{tier_limit}/{tier_limit} participants] {target_emoji}")
        tier = st.progress(0)
        for percent_complete in range(101):
            time.sleep(0.01)
            tier.progress(percent_complete, f"Total completion {math.trunc((tier_limit / tier_limit) * 100)} %")
    time.sleep(0.01 * Tyes_count * 2)