import { Injectable } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class ExCurricularService {

  constructor() { }

  form: FormGroup = new FormGroup ({
    $key: new FormControl(null),
    title: new FormControl('', Validators.required),
    monday: new FormControl(false),
    tuesday: new FormControl(false),
    wednesday: new FormControl(false),
    thursday: new FormControl(false),
    friday: new FormControl(false),
    timeFrom: new FormControl('', Validators.required),
    timeTo: new FormControl('', Validators.required),
  });

  initializeFormGroup() {
    this.form.setValue({
      $key: null,
      title: '',
      monday: false,
      tuesday: false,
      wednesday: false,
      thursday: false,
      friday: false,
      timeFrom: '',
      timeTo: '',
    });
  }

}
