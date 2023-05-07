from qiskit import IBMQ, Aer, transpile
from qiskit import QuantumCircuit
import math


def get_max_n(phase, shots):
    p_phase = 2 * math.pi * phase
    n = 0
    interval = [{"1": 0}, {"1": 0}]
    while math.sin(math.asin(math.sqrt(interval[0]["1"] / shots)) * 2) <=\
        math.sin(
        math.asin(math.sqrt(interval[1]["1"] / shots)) * 2
    ):
        n += 1
        qpe = QuantumCircuit(2, 1)
        qpe.x(1)
        qpe.h(0)
        qpe.cp(n * p_phase, 0, 1)
        qpe.h(0)
        qpe.measure(0, 0)
        aer_sim = Aer.get_backend("aer_simulator")
        t_qpe = transpile(qpe, aer_sim)
        results = aer_sim.run(t_qpe, shots=shots).result()
        answer = results.get_counts()
        if answer["1"] == shots:
            return n
        last_dic = interval[1]
        interval[1] = answer

        if interval[0]["1"] == 0:
            interval[0] = interval[1]
        else:
            interval[0] = last_dic

    if (
        math.acos(math.sqrt(interval[0]["0"] / shots)) * 2
        < math.acos(math.sqrt(interval[1]["0"] / shots)) * 2
    ):
        n -= 1
    elif (
        math.acos(math.sqrt(interval[0]["0"] / shots)) * 2 > math.pi / 2
        and math.acos(math.sqrt(interval[1]["0"] / shots)) * 2 > math.pi / 2
    ):
        n -= 2

    return n


def get_phase(phase, shots):
    p_phase = 2 * math.pi * phase
    n = get_max_n(phase, shots)
    qpe = QuantumCircuit(2, 1)
    qpe.x(1)
    qpe.h(0)
    qpe.cp(n * p_phase, 0, 1)
    qpe.h(0)
    qpe.measure(0, 0)
    aer_sim = Aer.get_backend("aer_simulator")
    t_qpe = transpile(qpe, aer_sim)
    results = aer_sim.run(t_qpe, shots=shots).result()
    answer = results.get_counts()
    experimental_phase =\
        math.asin(math.sqrt(answer["1"] / shots)) / (n * math.pi)
    return experimental_phase


if __name__ == "__main__":
    pass
