import tensorflow as tf
import tensorflow_probability as tfp

# Create a mixture of two Gaussians:
tfd = tfp.distributions
mix = 0.3
bimix_gauss = tfd.Mixture(
  cat=tfd.Categorical(probs=[mix, 1.-mix]),
  components=[
    tfd.Normal(loc=-1., scale=0.1),
    tfd.Normal(loc=+1., scale=0.5),
])

# Plot the PDF.
import matplotlib.pyplot as plt
x = tf.linspace(-2., 3., int(1e4)).numpy()
plt.plot(x, bimix_gauss.prob(x).numpy())
plt.show(block=True)

