import xml.etree.ElementTree as ET

def load_from_jff(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        states = []
        initial_state = None
        final_states = []
        for state in root.findall(".//state"):
            state_id = state.get("id")
            states.append(state_id)
            if state.find("initial") is not None:
                initial_state = state_id
            if state.find("final") is not None:
                final_states.append(state_id)

        transitions = []
        for transition in root.findall(".//transition"):
            from_state = transition.find("from").text
            to_state = transition.find("to").text
            symbol = transition.find("read").text if transition.find("read") is not None else None
            transitions.append({"from": from_state, "to": to_state, "symbol": symbol})

        return {
            "states": states,
            "initial_state": initial_state,
            "final_states": final_states,
            "transitions": transitions,
        }
    except Exception as e:
        raise ValueError(f"Erro ao carregar o arquivo JFLAP: {e}")
