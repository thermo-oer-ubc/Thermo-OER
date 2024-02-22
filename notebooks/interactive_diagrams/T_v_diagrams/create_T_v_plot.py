import ipywidgets as widgets
from IPython.display import display
import plotly.graph_objects as go
import pandas as pd

# Function to create and update the plot
def create_update_plot(fluid, entropy, temperature):
    df_liquid = pd.read_csv(f'{fluid}_T_s_liquid.csv')
    df_vapor = pd.read_csv(f'{fluid}_T_s_vapor.csv')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_liquid['Entropy Liquid (J/kg.K)'], y=df_liquid['Temperature (K)'],
                             mode='lines', name='Saturated Liquid'))
    fig.add_trace(go.Scatter(x=df_vapor['Entropy Vapor (J/kg.K)'], y=df_vapor['Temperature (K)'],
                             mode='lines', name='Saturated Vapor'))
    
    # Adding user input as a point
    fig.add_trace(go.Scatter(x=[entropy], y=[temperature], mode='markers', name='User Point'))

    fig.update_layout(title=f'{fluid} T-s Diagram', 
                      xaxis_title='Entropy (J/kg.K)', yaxis_title='Temperature (K)')
    fig.show()

# Dropdown widget for fluid selection
fluids = ['Water', 'Ammonia', 'R134a']  # Example fluid names
fluid_dropdown = widgets.Dropdown(options=fluids, value='Water', description='Fluid:')

# Text input widgets for entropy and temperature
entropy_input = widgets.FloatText(value=0, description='Entropy (J/kg.K):')
temperature_input = widgets.FloatText(value=0, description='Temperature (K):')

# Button to update the plot
update_button = widgets.Button(description='Update Plot')

# Display widgets
display(fluid_dropdown, entropy_input, temperature_input, update_button)

# Function to handle button click event
def on_button_clicked(b):
    create_update_plot(fluid_dropdown.value, entropy_input.value, temperature_input.value)

# Link the button click event to the function
update_button.on_click(on_button_clicked)
