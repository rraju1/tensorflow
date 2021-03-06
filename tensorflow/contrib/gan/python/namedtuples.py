# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Named tuples for TFGAN."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections


__all__ = [
    'GANModel',
    'InfoGANModel',
    'ACGANModel',
    'GANLoss',
    'GANTrainOps',
    'GANTrainSteps',
]


class GANModel(
    collections.namedtuple('GANModel', (
        'generator_inputs',
        'generated_data',
        'generator_variables',
        'generator_scope',
        'generator_fn',
        'real_data',
        'discriminator_real_outputs',
        'discriminator_gen_outputs',
        'discriminator_variables',
        'discriminator_scope',
        'discriminator_fn',
    ))):
  """A GANModel contains all the pieces needed for GAN training.

  Generative Adversarial Networks (https://arxiv.org/abs/1406.2661) attempt
  to create an implicit generative model of data by solving a two agent game.
  The generator generates candidate examples that are supposed to match the
  data distribution, and the discriminator aims to tell the real examples
  apart from the generated samples.

  Args:
    generator_inputs: The random noise source that acts as input to the
      generator.
    generated_data: The generated output data of the GAN.
    generator_variables: A list of all generator variables.
    generator_scope: Variable scope all generator variables live in.
    generator_fn: The generator function.
    real_data: A tensor or real data.
    discriminator_real_outputs: The discriminator's output on real data.
    discriminator_gen_outputs: The discriminator's output on generated data.
    discriminator_variables: A list of all discriminator variables.
    discriminator_scope: Variable scope all discriminator variables live in.
    discriminator_fn: The discriminator function.
  """


# TODO(joelshor): Have this class inherit from `GANModel`.
class InfoGANModel(
    collections.namedtuple('InfoGANModel', GANModel._fields + (
        'structured_generator_inputs',
        'predicted_distributions',
    ))):
  """An InfoGANModel contains all the pieces needed for InfoGAN training.

  See https://arxiv.org/abs/1606.03657 for more details.

  Args:
    structured_generator_inputs: A list of Tensors representing the random noise
      that must  have high mutual information with the generator output. List
      length should match `predicted_distributions`.
    predicted_distributions: A list of tf.Distributions. Predicted by the
      recognizer, and used to evaluate the likelihood of the structured noise.
      List length should match `structured_generator_inputs`.
  """


class ACGANModel(
    collections.namedtuple('ACGANModel', GANModel._fields +
                           ('one_hot_labels',
                            'discriminator_real_classification_logits',
                            'discriminator_gen_classification_logits',))):
  """An ACGANModel contains all the pieces needed for ACGAN training.

  See https://arxiv.org/abs/1610.09585 for more details.

  Args:
    one_hot_labels: A Tensor holding one-hot-labels for the batch.
    discriminator_real_classification_logits: Classification logits for real
      data.
    discriminator_gen_classification_logits: Classification logits for generated
      data.
  """


class GANLoss(
    collections.namedtuple('GANLoss', (
        'generator_loss',
        'discriminator_loss'
    ))):
  """GANLoss contains the generator and discriminator losses.

  Args:
    generator_loss: A tensor for the generator loss..
    discriminator_loss: A tensor for the discriminator loss.
  """


class GANTrainOps(
    collections.namedtuple('GANTrainOps', (
        'generator_train_op',
        'discriminator_train_op',
        'global_step_inc_op'
    ))):
  """GANTrainOps contains the training ops.

  Args:
    generator_train_op: Op that performs a generator update step.
    discriminator_train_op: Op that performs a discriminator update step.
    global_step_inc_op: Op that increments the shared global step.
  """


class GANTrainSteps(
    collections.namedtuple('GANTrainSteps', (
        'generator_train_steps',
        'discriminator_train_steps'
    ))):
  """Contains configuration for the GAN Training.

  Args:
    generator_train_steps: Number of generator steps to take in each GAN step.
    discriminator_train_steps: Number of discriminator steps to take in each GAN
      step.
  """
