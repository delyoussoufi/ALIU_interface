import { TestBed } from '@angular/core/testing';

import { ArtDataService } from './art-data.service';

describe('ArtDataService', () => {
  let service: ArtDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ArtDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
