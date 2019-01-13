import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExCurricularComponent } from './ex-curricular.component';

describe('ExCurricularComponent', () => {
  let component: ExCurricularComponent;
  let fixture: ComponentFixture<ExCurricularComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExCurricularComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExCurricularComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
