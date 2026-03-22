import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS
import datetime

st.set_page_config(
    page_title="Calendar - CSM",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Auth guard
if not st.session_state.get("logged_in"):
    st.switch_page("pages/streamlit_login.py")

if st.session_state.get("role") == "admin":
    st.switch_page("pages/admin_dashboard.py")

# Calendar CSS
st.markdown("""
<style>
.calendar-container {
    display: flex;
    height: 80vh;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
}
.calendar-sidebar {
    width: 25%;
    border-right: 1px solid #e0e0e0;
    background-color: #f8f9fa;
    overflow-y: auto;
}
.calendar-main {
    width: 75%;
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
}
.calendar-header {
    padding: 1rem;
    background-color: #A87B33;
    color: white;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.calendar-grid {
    flex: 1;
    padding: 1rem;
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 1px;
    background-color: #e0e0e0;
}
.calendar-day {
    background-color: #ffffff;
    padding: 0.5rem;
    min-height: 80px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.calendar-day:hover {
    background-color: #f0f0f0;
}
.calendar-day.today {
    background-color: #e8f5e8;
}
.calendar-day.selected {
    background-color: #fff3cd;
}
.event-item {
    background-color: #A87B33;
    color: white;
    padding: 0.2rem;
    border-radius: 3px;
    font-size: 0.7rem;
    margin-bottom: 0.2rem;
    cursor: pointer;
}
.event-item:hover {
    background-color: #8C662A;
}
.notes-section {
    padding: 1rem;
    border-top: 1px solid #e0e0e0;
    background-color: #f8f9fa;
}
.day-header {
    font-weight: bold;
    color: #A87B33;
    margin-bottom: 0.5rem;
}
.event-detail {
    background-color: #ffffff;
    padding: 1rem;
    border-radius: 5px;
    margin-bottom: 0.5rem;
    border-left: 4px solid #A87B33;
}
</style>
""", unsafe_allow_html=True)

# Header
col_title, col_back = st.columns([6, 1])
with col_title:
    st.markdown("### 📅 Calendar")
with col_back:
    if st.button("← Back", use_container_width=True):
        st.switch_page("pages/user_dashboard.py")

st.divider()

# Initialize calendar state
if "selected_date" not in st.session_state:
    st.session_state.selected_date = datetime.date.today()

# Sample events data
events = {
    datetime.date(2024, 3, 22): [
        {"title": "Team Meeting", "time": "10:00 AM", "type": "meeting"},
        {"title": "Project Deadline", "time": "5:00 PM", "type": "deadline"}
    ],
    datetime.date(2024, 3, 25): [
        {"title": "Client Call", "time": "2:00 PM", "type": "call"},
        {"title": "Review Session", "time": "4:00 PM", "type": "review"}
    ],
    datetime.date(2024, 3, 28): [
        {"title": "Presentation", "time": "11:00 AM", "type": "presentation"}
    ]
}

# Calendar Interface
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown("**My Calendar**")
    
    # Month navigation
    current_month = st.session_state.selected_date.replace(day=1)
    prev_month = current_month - datetime.timedelta(days=1)
    next_month = current_month + datetime.timedelta(days=32)
    next_month = next_month.replace(day=1)
    
    col_prev, col_month, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("←", use_container_width=True):
            st.session_state.selected_date = prev_month
            st.rerun()
    with col_month:
        st.markdown(f"**{current_month.strftime('%B %Y')}**")
    with col_next:
        if st.button("→", use_container_width=True):
            st.session_state.selected_date = next_month
            st.rerun()
    
    st.markdown("---")
    
    # Mini calendar
    year, month = st.session_state.selected_date.year, st.session_state.selected_date.month
    
    # Calculate calendar grid
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    start_weekday = first_day.weekday()
    
    # Weekday headers
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    cols = st.columns(7)
    for i, day in enumerate(weekdays):
        with cols[i]:
            st.markdown(f"<div style='text-align: center; font-weight: bold; font-size: 0.8rem;'>{day}</div>", unsafe_allow_html=True)
    
    # Calendar days
    day = 1
    for week in range(6):
        cols = st.columns(7)
        for weekday in range(7):
            with cols[weekday]:
                if week == 0 and weekday < start_weekday:
                    st.markdown("")
                elif day > last_day.day:
                    st.markdown("")
                else:
                    current_date = datetime.date(year, month, day)
                    is_today = current_date == datetime.date.today()
                    is_selected = current_date == st.session_state.selected_date
                    has_events = current_date in events
                    
                    bg_color = "#fff3cd" if is_selected else "#e8f5e8" if is_today else "#ffffff"
                    
                    st.markdown(f"""
                    <div style='text-align: center; padding: 0.5rem; background-color: {bg_color}; border-radius: 5px; cursor: pointer; {"border: 1px solid #A87B33;" if is_selected else ""}'>
                        <div style='font-weight: bold;'>{day}</div>
                        {f"<div style='width: 4px; height: 4px; background-color: #A87B33; border-radius: 50%; margin: 0 auto;'></div>" if has_events else ""}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"Select {day}", key=f"select_{day}", use_container_width=True):
                        st.session_state.selected_date = current_date
                        st.rerun()
                    
                    day += 1
        
        if day > last_day.day:
            break
    
    st.markdown("---")
    st.markdown("**Notes**")
    notes = st.text_area("Add notes for today:", height=100, key="daily_notes")
    if st.button("Save Notes", use_container_width=True):
        st.success("Notes saved!")

with col_main:
    # Calendar header
    st.markdown(f"""
    <div class="calendar-header">
        <span>{st.session_state.selected_date.strftime('%B %d, %Y')}</span>
        <span>Personal Calendar</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Events for selected date
    selected_events = events.get(st.session_state.selected_date, [])
    
    if selected_events:
        st.markdown(f"**{len(selected_events)} Events**")
        for event in selected_events:
            st.markdown(f"""
            <div class="event-detail">
                <div style="font-weight: bold;">{event['title']}</div>
                <div style="color: #666; font-size: 0.9rem;">🕐 {event['time']} • {event['type'].title()}</div>
                <div style="margin-top: 0.5rem;">
                    <button style='background-color: #A87B33; color: white; border: none; padding: 0.3rem 0.8rem; border-radius: 5px; margin-right: 0.5rem;'>Edit</button>
                    <button style='background-color: #dc3545; color: white; border: none; padding: 0.3rem 0.8rem; border-radius: 5px;'>Delete</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; color: #999;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">📅</div>
            <div>No events scheduled for this day</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add new event
    st.markdown("---")
    st.markdown("**Add New Event**")
    col_title, col_time, col_type = st.columns([2, 1, 1])
    with col_title:
        event_title = st.text_input("Event Title")
    with col_time:
        event_time = st.time_input("Time")
    with col_type:
        event_type = st.selectbox("Type", ["meeting", "call", "deadline", "presentation", "review"])
    
    if st.button("Add Event", type="primary"):
        if event_title:
            st.success("Event added successfully!")
            st.rerun()
        else:
            st.error("Please enter an event title")
    
    # Daily notes
    st.markdown("---")
    st.markdown("**Daily Notes**")
    st.markdown(f"""
    <div class="notes-section">
        <div class="day-header">Notes for {st.session_state.selected_date.strftime('%B %d, %Y')}</div>
        <div style="background-color: #ffffff; padding: 1rem; border-radius: 5px; min-height: 100px;">
            Today's focus: Complete project documentation and prepare for tomorrow's presentation.
        </div>
    </div>
    """, unsafe_allow_html=True)
