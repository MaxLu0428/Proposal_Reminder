import os
import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Proposal, vDRM
from .forms import ProposalForm, SelectDRMForm, UploadFileForm
from difflib import HtmlDiff

