import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Orientacion(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  
    elif val > 0:
        return 1  
    else:
        return 2  

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    hull = []

    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x:
            l = i

    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if Orientacion(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

def plot_points(points):
    x = [point.x for point in points]
    y = [point.y for point in points]
    plt.scatter(x, y, color='red')

def plot_convex_hull(hull):
    x = [point.x for point in hull]
    y = [point.y for point in hull]
    x.append(hull[0].x)
    y.append(hull[0].y)
    plt.plot(x, y, color='blue')

def main():
    points = []
    n = int(input("Ingrese la cantidad de puntos: "))

    for i in range(n):
        x, y = map(int, input(f"Ingrese las coordenadas del punto {i+1}: ").split())
        points.append(Punto(x, y))

    hull = convex_hull(points)

    plot_points(points)
    plot_convex_hull(hull)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Convex Hull')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
