class AutomatonValidator:
    def __init__(self, automaton_data):
        self.states = automaton_data.get("states", [])
        self.initial_state = automaton_data.get("initial_state")
        self.final_states = automaton_data.get("final_states", [])
        self.transitions = automaton_data.get("transitions", [])

    def validate(self):
        print("\n" + "=" * 40)
        print("RESULTADO DA VALIDAÇÃO DO AUTÔMATO")
        print("=" * 40 + "\n")

        errors = set()

        print("1. Validando os Estados".center(40, "-"))
        if not self.states:
            print("❌ Nenhum estado foi definido.")
            errors.add("Nenhum estado foi definido.")
        else:
            print(f"✅ Estados definidos: {self.states}")

        print("\n" + "2. Validando o Estado Inicial".center(40, "-"))
        if self.initial_state not in self.states:
            print(f"❌ Estado inicial inválido ({self.initial_state})")
            errors.add(f"Estado inicial inválido: {self.initial_state}")
        else:
            print(f"✅ Estado inicial válido: {self.initial_state}")

        print("\n" + "3. Validando os Estados Finais".center(40, "-"))
        if not self.final_states:
            print("⚠️ Aviso: Nenhum estado final foi definido.")
        else:
            print(f"✅ Estados finais definidos: {self.final_states}")

        invalid_finals = [state for state in self.final_states if state not in self.states]
        if invalid_finals:
            print(f"❌ Estados finais inválidos: {invalid_finals}")
            errors.add(f"Estados finais inválidos: {invalid_finals}")
        else:
            print("✅ Todos os estados finais são válidos.")

        print("\n" + "4. Validando as Transições".center(40, "-"))
        if not self.transitions:
            print("⚠️ Aviso: Nenhuma transição foi definida.")
        else:
            for transition in self.transitions:
                from_state = transition["from"]
                to_state = transition["to"]
                symbol = transition["symbol"]

                if from_state not in self.states or to_state not in self.states:
                    print(f"❌ Transição inválida: {from_state} --({symbol})--> {to_state}")
                    errors.add(f"Transição inválida: {transition}")
                else:
                    print(f"✅ Transição válida: {from_state} --({symbol})--> {to_state}")

        # Resumo
        print("\n" + "=" * 40)
        print("RESUMO".center(40, "="))
        if not errors:
            print("🎉 Autômato válido! 🎉")
            return "Autômato válido"
        else:
            error_summary = ", ".join(errors)
            print(f"❌ Erro(s) encontrado(s): {error_summary}")
            return f"Erro(s) encontrado(s): {error_summary}"

    def validate_input(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            transition = next(
                (t for t in self.transitions if t["from"] == current_state and t["symbol"] == symbol),
                None
            )
            if not transition:
                return f"❌ Entrada '{input_string}' rejeitada: Sem transição para '{symbol}' a partir de '{current_state}'."
            current_state = transition["to"]

        if current_state in self.final_states:
            return f"✅ Entrada '{input_string}' aceita. Estado final: {current_state}."
        else:
            return f"❌ Entrada '{input_string}' rejeitada. Estado final: {current_state}."
