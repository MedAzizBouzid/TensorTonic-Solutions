def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    centroids = []
    i = 0

    while i < k:
        count = 0
        
        # create a list of zeros same size as a point
        sums = [0] * len(points[0])

        j = 0
        while j < len(points):
            if assignments[j] == i:
                d = 0
                while d < len(points[j]):
                    sums[d] += points[j][d]
                    d += 1
                count += 1
            j += 1

        if count != 0:
            c = []
            d = 0
            while d < len(sums):
                c.append(sums[d] / count)
                d += 1
        else:
            c = [0] * len(points[0])

        centroids.append(c)
        i += 1

    return centroids