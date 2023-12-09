import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParentSearchInfoComponent } from './parent-search-info.component';

describe('ParentSearchInfoComponent', () => {
  let component: ParentSearchInfoComponent;
  let fixture: ComponentFixture<ParentSearchInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ParentSearchInfoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ParentSearchInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
